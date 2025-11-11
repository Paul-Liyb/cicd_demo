import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(input_size, output_size)
    
    def forward(self, x):
        return self.linear(x)

# 我们可以定义一个辅助函数来创建模型实例
def create_model():
    # 假设我们的模型接收 10 维输入, 输出 2 维
    return SimpleModel(input_size=10, output_size=2)