import numpy as np
import torch
from application.tools.inference import get_final_preds
from torchvision import transforms

def validate(img_input, model, c, s):

    if isinstance(img_input, np.ndarray):
        transform = transforms.Compose([
        transforms.ToTensor(),          
    ])
        img_input = transform(img_input)
        
    if torch.cuda.is_available():
        img_input = img_input.cuda()

    # 增加一個維度[b,c,w,h]
    img_input = img_input.unsqueeze(0)
    
    model.eval()
    with torch.no_grad():
        outputs = model(img_input)
        if isinstance(outputs, list):
            output = outputs[-1]
        else:
            output = outputs
    preds, maxvals= get_final_preds(output.clone().cpu().numpy(), c, s)  # 利用泰勒展開座標轉換      
    
    return preds

