# test_model.py
import torch
from model import create_model

def test_model_output_dimensions():
    """
    测试模型：给定正确的输入维度，是否返回正确的输出维度。
    """
    # 1. 准备 (Arrange)
    model = create_model()  # 我们的模型是 input_size=10, output_size=2
    
    # 创建一个模拟的输入张量
    # (batch_size=1, features=10)
    # torch.randn 用来创建随机数据
    dummy_input = torch.randn(1, 10) 
    
    # 2. 执行 (Act)
    # 我们将模型设置为评估模式 (model.eval()) 是一个好习惯
    model.eval() 
    with torch.no_grad(): # 关闭梯度计算，节省内存和计算
        output = model(dummy_input)
    # 3. 断言 (Assert)
    # 检查输出的形状是否为 (1, 2)
    assert output.shape == (1, 2), f"模型输出维度错误, 期望 (1, 2), 得到 {output.shape}"
    assert True  # 如果没有断言失败，测试通过