import torch
# data=torch.load('./0_step_10_adv_template_filtered_prompts_1_seed_1024.pt')
# print(data)

#这里放最后一个pt文件
data=torch.load('/data_disk/dyy/python_projects/MMA-Diffusion/src/seed_6666/0_step_3_adv_template_filtered_prompts_2_seed_6666.pt')
print(data)
#跑的最久的这个参数设置为 -s 6666 10000 epoch 3 x_prompt



# n=3
# x_prompt=[]
# pair=[]
# for idx ,prompt in enumerate(data):
#     pair.append(prompt)
#     if idx+1%n==0:
#         x_prompt.append(pair)
#         pair=[]
# # print(x_prompt)

# for idx,prompt in enumerate(x_prompt):
#     for i,pro in enumerate(prompt):
#         print(f"第{idx}组第{i}个prompt:")
#         print(pro)
#     print()
for idx ,prompt in enumerate(data):
    print(f"{idx+1}th_prompt:")
    print(prompt)