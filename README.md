# kaiwu-examples

[English Version](README-EN.md)

一个量子优化问题的Python 案例包。其中示例4 tutorial4_cimoptimizer.py 演示了通过 kw.cim.CIMOptimizer 提交真机任务的流程

## 项目结构

```
kaiwu_examples/
└── tutorial/
    ├── tutorial1_qubo_matrix.py
    ├── tutorial2_tsp.py
    ├── tutorial3_max_cut.py
    └── tutorial4_cimoptimizer.py
```

## 安装要求

- Python 3.8+
- NumPy >= 1.19.0
- Pandas >= 1.0.0
- Matplotlib >= 3.0.0
- Networkx >= 2.0
- Pytest >= 7.0.0 (用于测试)

## 安装

```bash
# 推荐使用 conda 创建新环境
conda create -n quantum_env python=3.8
conda activate quantum_env

# 安装依赖
pip install -r requirements.txt

# 开发模式安装
pip install -e .
```

## 快速开始

### kaiwu-sdk 依赖包 安装说明（必填）

详细内容请访问 [kaiwu-sdk 下载地址](https://platform.qboson.com/sdkDownload) （无权限，请注册账号再访问）

详细文档请访问 [kaiwu-sdk 安装说明](https://kaiwu-sdk-docs.qboson.com/zh/source/sdk_installation_instructions.html)

获取真机调用资格需要先获取账号的 SDK 授权信息：

```
用户ID: <your-user-id>
SDK授权码: <your-sdk-token>
```

> 请将以上信息替换为您的实际授权信息

## 案例示例

### 经典优化问题
- [QUBO矩阵](tutorial/tutorial1_qubo_matrix.py): 基础QUBO模型构建和求解
- [TSP问题](tutorial/tutorial2_tsp.py): 旅行商问题的QUBO建模
- [Max Cut问题](tutorial/tutorial3_max_cut.py): 最大割问题求解示例
- [提交TSP任务到真机](tutorial/tutorial4_cimoptimizer.py): TSP问题使用真机求解示例

### 经典优化问题(notebook)
- [QUBO矩阵](tutorial/notebook/tutorial1_qubo_matrix.ipynb): 基础QUBO模型构建和求解
- [TSP问题](tutorial/notebook/tutorial2_tsp.ipynb): 旅行商问题的QUBO建模
- [Max Cut问题](tutorial/notebook/tutorial3_max_cut.ipynb): 最大割问题求解示例


## 开发指南

### 案例运行
```bash
python tutorial/tutorial1_qubo_matrix.py

python tutorial/tutorial2_tsp.py

python tutorial/tutorial3_max_cut.py

python tutorial/tutorial4_cimoptimizer.py
```

### 代码风格
- 遵循PEP 8规范
- 使用类型注解
- 编写详细的文档字符串

## 文档

详细文档请访问 [documentation](https://kaiwu-sdk-docs.qboson.com/zh/source/introduction.html)

## 贡献指南

欢迎提交 Pull Requests！请确保遵循以下步骤：

1. Fork 本项目
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

### 贡献前准备
- 确保所有测试通过
- 更新相关文档
- 添加必要的单元测试
- 遵循代码规范

## 许可证

本项目采用 apache 2.0 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

