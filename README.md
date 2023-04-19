# MakePictureClearer
 基于Streamlit搭建的图像增强web应用
 ## 使用方法
 安装streamlit库
 用以下指令
 pip install streamlit_apex_charts -i https://pypi.tuna.tsinghua.edu.cn/simple
 打开main.py文件，根据注释填入自己的AK和SK
 最后运行命令“streamlit run main.py的文件路径”
 ## 模型
百度AI开放平台使用OAuth2.0授权调用开放了API，我在这个项目里调用了这个API，使用了其中的图像处理模型。说实话，作为新手，调用百度的模型比想象中的难不少（修bug修到了凌晨两点）。
 ## 总结
 此项目只是我练习使用Streamlit库的时候做的。其中的图像处理模型，我想等我有一定技术积累后，自己写一个，因为图像处理看似简单，实则有很多细节问题需要考虑。总之，这个项目还未结束。