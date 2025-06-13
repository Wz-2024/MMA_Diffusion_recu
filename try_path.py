import torch

# 加载 .pt 文件
data = torch.load('/data_disk/dyy/python_projects/MMA-Diffusion/src/seed_6666/0_step_10000_adv_template_filtered_prompts_2_seed_6666.pt')

# 打印数据
print(data)

# 检查数据类型
print(type(data))
for idx,prompt in enumerate(data):
    print(idx,prompt)
