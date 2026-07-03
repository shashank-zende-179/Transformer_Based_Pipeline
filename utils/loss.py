import torch.nn.functional as F

def hybrid_loss(output, target):
    l1 = F.l1_loss(output, target)
    mse = F.mse_loss(output, target)

    return l1 + 0.5 * mse

