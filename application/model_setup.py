import torch
import yaml
from application.models.transpose_h import TransPoseH


def load_config(yaml_path):
    with open(yaml_path, 'r') as file:
        cfg = yaml.safe_load(file)
    return cfg

def main():
    cfg = load_config('./application/config/TP_H_w48_256x192_d96_h192_relu_enc6_mh1.yaml')
    model = TransPoseH(cfg)
    
    if torch.cuda.is_available():
        # 若有 GPU，則將模型載入到 GPU
        ckpt_state_dict = torch.load(cfg['TEST']['MODEL_FILE'])
        model.load_state_dict(ckpt_state_dict, strict=True)
        model = torch.nn.DataParallel(model).cuda()
    else:
        # 若無 GPU，則將模型載入到 CPU
        ckpt_state_dict = torch.load(cfg['TEST']['MODEL_FILE'], map_location=torch.device('cpu'), weights_only=True)
        model.load_state_dict(ckpt_state_dict, strict=True)
        model = torch.nn.DataParallel(model).to('cpu')
    return model, cfg
