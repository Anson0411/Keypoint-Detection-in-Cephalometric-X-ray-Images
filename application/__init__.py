from flask import Flask, request, render_template, redirect, url_for
from flask_cors import CORS
import cv2
import os
import numpy as np
import application.model_setup as model_setup
import application.img_transform as img_transform
import application.predict as predict


app = Flask(
    __name__,
    static_folder = 'result', # 靜態檔案的資料夾名稱
    static_url_path = '/'     # 靜態檔案的對應的網址路徑
) 
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESSED_FOLDER'] = './application/result'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True) 

# 載入模型數據
ht_model, cfg = model_setup.main()

@app.route('/')
def index():
    return render_template('upload.html')  #

@app.route('/upload', methods=['POST'])
def upload():
    # 確認request中有 'image' 
    if 'image' not in request.files:
        return "No file part in the request"
    
    file = request.files['image']
    
    # 檢查是否為 TIFF 
    if file and (file.filename.endswith('.tiff') or file.filename.endswith('.tif')):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)  
        
        img = cv2.imread(filepath)
        input, c, s = img_transform.img_resize(img, cfg) # 影像處理
        preds = predict.validate(input, ht_model, c, s) # 輸入模型預測
   
        # 圖片繪製預測點位
        if len(preds) > 0 and isinstance(preds[0], np.ndarray):
            coords = preds[0]  
            
            for point in coords:
                x, y = int(point[0]), int(point[1])
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)  # 標記
                cv2.putText(img, f'({x}, {y})', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0)) # 顯示座標

            processed_filepath = os.path.join(app.config['PROCESSED_FOLDER'], 'processed_' + file.filename + '.png') 
            cv2.imwrite(processed_filepath, img)  # 儲存處理後的圖片

            # 將座標轉換列表
            coordinates = coords.tolist()
            rounded_coordinates = [[round(x, 2), round(y, 2)] for x, y in coordinates]
            image_path='processed_' + file.filename+ '.png'

            return render_template('display.html', image_path=image_path, coordinates=rounded_coordinates)
    else:
        return "Only TIFF files are allowed"

if __name__ == '__main__':
    app.run(debug=True)




