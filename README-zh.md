<img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version">
<img src="https://img.shields.io/badge/License-Apache%202.0-green" alt="License">

## 项目简介

`kaiwu-basic-examples` 是一个专注于量子优化问题的开源案例集，旨在通过实践帮助开发者和研究人员快速入门量子优化领域。本项目为希望从零开始学习量子优化的用户提供了系统化的学习路径，涵盖从基础概念到实际案例的全流程，社区的目标是：

- **普及知识**：帮助用户理解量子优化问题的核心概念及其建模方法。更多请参考 [社区文档](https://kaiwu.qboson.com/plugin.php?id=knowledge)。
- **实践能力**：通过真实案例学习如何使用 Python 实现量子优化算法。
- **社区成长**：培养用户从学习者到社区贡献者的转变，推动社区共同进步。

本项目不仅是一个工具，更是一个学习与成长的平台。无论您是量子计算的新手，还是有经验的开发者，都可以从中获益。

## 贡献指南

### 贡献的意义

通过参与本项目，您不仅可以加深对量子优化问题的理解，还能为社区贡献力量，帮助其他学习者成长；另外我们也在量子开发实验室中，提供前沿的技术研究课题，并予以贡献者一定的奖励，希望通过您的参与，逐步建立一个充满活力的学习型、贡献型社区。

### 如何开始贡献？

1. **报告问题**：
   - 如果您发现 Bug 或有改进建议，请在 GitHub Issues 中提交。
   - 提交时请描述清楚问题背景和复现步骤。

2. **贡献代码**： 
   - 根据任务要求，编写代码实现。
   - 通过 Fork 仓库、创建分支的方式提交代码。
   - 提交前请确保代码通过测试，并符合项目规范。

3. **参与讨论**：
   - 在 GitHub Discussions 中参与功能讨论或分享经验。

### 代码提交流程

1. **Fork 仓库**：
   - 点击 `Fork` 按钮，将项目复制到自己的账户。

2. **克隆代码**：
   ```bash
   git clone https://github.com/用户名/kaiwu-basic-examples.git
   cd kaiwu-basic-examples
   ```

3. **创建分支**：
   ```bash
   git checkout -b feature/功能名称
   ```

4. **提交代码**：
   ```bash
   git add .
   git commit -m "描述提交内容"
   git push origin feature/功能名称
   ```

5. **发起 Pull Request**：
   - 在 GitHub 上点击 `New Pull Request`，填写更改说明。

## 快速开始

### 安装要求

- Python 3.10+
- NumPy >= 1.19.0
- Pandas >= 1.0.0
- Matplotlib >= 3.0.0
- Networkx >= 2.0
- Pytest >= 7.0.0 (用于测试)

### 代码风格

- 遵循PEP 8规范
- 使用类型注解
- 编写详细的文档字符串

### 安装步骤

1. **创建并激活环境**：
   ```bash
   # 推荐使用 conda 创建新环境
   conda create -n quantum_env python=3.8
   conda activate quantum_env
   ```

2. **克隆本仓库到本地**：
   ```bash
   git clone https://github.com/QBosonCommunity/kaiwu-basic-examples.git
   cd kaiwu-basic-examples
   ```

3. **安装依赖包**：
   ```bash
   pip install -r requirements.txt
   ```

4. **开发模式安装（可选）**：
   ```bash
   pip install -e .
   ```

### kaiwu-sdk 安装说明（必需）

在开始使用之前，您需要安装 kaiwu-sdk 依赖包：

1. **获取 SDK**：
   - 访问 [kaiwu-sdk 下载地址](https://platform.qboson.com/sdkDownload)（需要注册账号）
   - 查看 [kaiwu-sdk 安装说明](https://kaiwu-sdk-docs.qboson.com/zh/source/sdk_installation_instructions.html)

2. **配置授权信息**：
   获取您的 SDK 授权信息：
   ```
   用户ID: <your-user-id>
   SDK授权码: <your-sdk-token>

   ```
   > 请将以上信息替换为您的实际授权信息

### 获取真机调用资格

为了帮助用户体验量子计算的实际应用，您可以按照以下步骤获取真机调用资格：

1. 注册 [相干光量子计算云平台](https://platform.qboson.com/)账号。
2. 完成平台的 SDK 新手引导并获取真机调用额，参考 [文档](https://platform.qboson.com/resource/beginner_tutorial)。 

### 运行第一个案例
```python
  代码中的这行代码替换成如下的例子代码
  kw.license.init(user_id="xxxxxxx", sdk_code="xxxxxxx")
  
  例如： 非真实账号，如需要请登录云平台申请获取
  kw.license.init(user_id="39302589031902227330" sdk_code="v1A22GNmyhP063a4t7Osa2HsAMkuaB")

```

以下是运行 QUBO 矩阵的构建和求解的示例代码：

```python
python tutorial/tutorial1_qubo_matrix.py
```

通过此案例，您可以快速调用函数并进行求解。

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

## 目录结构

```
kaiwu-basic-examples/
├── examples/ 
│   ├── qubo_matrix_modeling.py     # QUBO 矩阵建模案例
│   ├── traveling_salesman.py       # 旅行商问题案例
│   ├── max_cut.py                  # 最大割问题案例
│   └── optimization.py             # 量子计算机提交任务实践
├── requirements.txt                # 依赖包列表
├── setup.py                        # 安装脚本
└── README.md                       # 本文档
```

## 社区与支持

1. **提问和讨论**：
   - [GitHub Discussions](https://github.com/QBosonCommunity/kaiwu-basic-examples/discussions)

2. **报告问题**：
   - [GitHub Issues](https://github.com/QBosonCommunity/kaiwu-basic-examples/issues)

3. **邮件联系**：
   - business@boseq.com

## 致谢

- 感谢所有贡献者的宝贵贡献。
- 感谢量子计算社区贡献者的支持和反馈。
