# 结构
- mininet生成训练或者实验环境
- redis pub/sub作为中间消息通道
- streamlit订阅通道实现前端显示

# dependency

### mininet
https://zhuanlan.zhihu.com/p/576832894

### streamlit
pip install streamlit
pip install --upgrade protobuf

### redis-py & redis
sudo apt install redis
pip install redis

### gym & gym-rlcc
pip install gym

cd gym-rlcc
pip install -e .

# usage
启动:
`cd tmp
sudo python ../train.py
`

`
cd to rllib
python train.py
`
`
cd webui
streamlit run app.py
`