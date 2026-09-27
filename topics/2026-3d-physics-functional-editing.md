# 2026 年 3D 物理资产与功能编辑：100 篇论文专题

> 跨日期专题，统计 2026-01-01 至 2026-09-27 首次提交到 arXiv 的论文；**不是 2026-09-27 当日 New submissions 日报**。本页聚焦一个问题：怎样用测试时 3D 编辑、少量物理探测与仿真反馈，让生成的可形变资产在新载荷下真正发挥目标功能？

## 论文卡片

按与上述问题的关系精选；下方保留 100 篇完整目录。卡片不附未经核验的配图。

| 论文 | 论文 | 论文 |
|---|---|---|
| <sub>功能驱动几何 · Purdue University</sub><br>**[PG-3DGS](https://arxiv.org/abs/2605.11266)**<br>用可微物理目标编辑 3D Gaussian 几何，并报告打印飞机的升力测试。<br>[Paper](https://arxiv.org/abs/2605.11266) · [机构/正文](https://arxiv.org/html/2605.11266) | <sub>可形变资产生成 · Nankai University</sub><br>**[DeformSmith](https://arxiv.org/abs/2609.18620)**<br>从文本或单图生成资产，以物理探针和仿真反馈调整，并用操作任务评价；真实物理保真需进一步核查。<br>[Paper](https://arxiv.org/abs/2609.18620) · [机构/正文](https://arxiv.org/html/2609.18620) | <sub>受力物性校准 · Tuojing Intelligence / Southeast University</sub><br>**[KnockGS](https://arxiv.org/abs/2608.27365)**<br>利用已知施力校准弹性与密度尺度，并评价新方向和强度的作用力响应。<br>[Paper](https://arxiv.org/abs/2608.27365) · [机构/正文](https://arxiv.org/html/2608.27365) |
| <sub>几何与材料共优化 · Cornell University</sub><br>**[Multimaterial 3D Printing](https://arxiv.org/abs/2607.13174)**<br>用实测拟合的超弹性本构律优化结构拓扑与材料组分；最终打印方案的功能增益尚需核查。<br>[Paper](https://arxiv.org/abs/2607.13174) · [机构/正文](https://arxiv.org/html/2607.13174) | <sub>异质柔体可微求解 · National Taiwan University / NUS / UBC 等</sub><br>**[DiffPhD](https://arxiv.org/abs/2605.14526)**<br>提供含异质材料与接触的可微 3D 动力学求解器和梯度检查。<br>[Paper](https://arxiv.org/abs/2605.14526) · [机构/正文](https://arxiv.org/html/2605.14526) | <sub>单图物理装配 · Carnegie Mellon University</sub><br>**[SNAP3D](https://arxiv.org/abs/2609.13146)**<br>修改部件连接与接触几何，并用重力稳定性和真实装配检验。<br>[Paper](https://arxiv.org/abs/2609.13146) · [机构/正文](https://arxiv.org/html/2609.13146) |

## 检索概况

- **时间与去重：**以 arXiv `v1` 首次提交日为准，覆盖 2026-01-01 至 2026-09-27；100 个不同 arXiv ID。预印本首发日不等于会议或期刊录用日。
- **来源：**标题、日期和摘要来自 arXiv；机构依据论文 HTML 作者栏或 PDF 首页核对。每条目录给出论文与机构证据链接。变量及评价方式主要依据摘要，少量边界条目补查正文；这不是 100 篇全文复现报告。
- **筛选：**只纳入具有明确 3D 几何、材料、接触、动力学或流体变量，并连到物理仿真、方程、力学测试或功能任务的工作。机构为可核对的研究型高校、科研院所或成熟工业研究团队；这个口径并非统一大学排名。排除仅做外观渲染、一般视频生成、纯 2D 与仅在题名使用“physical”的工作。
- **关联度：**“核心”表示 3D 物理变量与评价直接相关；“相邻”表示提供资产、求解器、数据或评价部件。100 篇并不都是测试时可形变功能编辑的直接先例。

| 方向 | 篇数 | 核心 | 相邻 |
| --- | ---: | ---: | ---: |
| 物性与动力学反演 | 25 | 17 | 8 |
| 可交互物理场景与资产 | 29 | 23 | 6 |
| 可形变资产与材料功能编辑 | 15 | 12 | 3 |
| 结构、接触与流体逆向设计 | 23 | 20 | 3 |
| 求解器、神经算子与基准 | 8 | 8 | 0 |
| **合计** | **100** | **80** | **20** |

## 一个待解决的具体问题

**任务定义。** 输入单图生成的 3D 资产、允许编辑的局部区域、目标功能，以及预算内 1–3 次**已知载荷**探测。输出修改后的几何和空间材料场。编辑后冻结资产，用训练或校准阶段未见过的载荷、接触位置与边界条件检验功能：例如指定弯曲、稳定夹持、能量吸收。单图只提供几何和材料先验；真实刚度、质量与摩擦不能仅凭外观唯一辨识。

**测试时变量。** 在保持外观和可制造性的约束下，编辑局部几何 $G$、杨氏模量 $E(x)$、泊松比 $\nu(x)$、密度 $\rho(x)$；只有存在可观测接触证据时再加入摩擦 $\mu(x)$。先用已知力和位移拟合候选物性，再在目标工况下优化形状与材料。这里的 TTT 指冻结通用生成器后，针对**一个给定资产**进行有预算的参数或几何更新。

**仿真 agent 的职责。** 生成可执行的载荷和边界条件，从候选探测中挑选最能区分材料假设的 1–3 个动作，读取应变集中、滑移或碰撞失败位置，决定下一处局部编辑及何时停止。连续参数的梯度更新仍由 FEM/MPM 或受预算约束的优化器完成；agent 的价值需在**相同仿真次数**下与固定探针、随机探针和无 agent 搜索比较。

**关键区别。** 物性辨识看已知探测是否解释了观测；功能设计看冻结后是否能在未见载荷达到目标。若只在校准探针上提高拟合，尚不能称资产已经“物理有用”。

## Top papers：最贴近问题的 12 篇

按“直接近邻 → 物性/求解方法 → 资产与评价支撑”排序，非论文质量排名。

| # | 论文与机构 | 已经解决的一步 `[事实]` | 仍要验证的一环 `[推断]` |
| ---: | --- | --- | --- |
| 1 | [PG-3DGS](https://arxiv.org/abs/2605.11266) · Purdue | 可微物理目标优化 3DGS 几何；打印飞机升力测试 | 加入可形变材料场和未见受力响应 |
| 2 | [DeformSmith](https://arxiv.org/abs/2609.18620) · Nankai | 层级生成可形变资产，以物理探针和仿真反馈调整，并评价操作任务 | 逐资产测试时联合编辑及独立真实物理复核 |
| 3 | [Towards end-to-end optimization in multimaterial 3D printing](https://arxiv.org/abs/2607.13174) · Cornell | 实测拟合本构律，联合优化拓扑和材料组分 | 连到单图生成资产及未见载荷的实物功能测试 |
| 4 | [Topology-Optimized Pneumatic Soft Actuator](https://arxiv.org/abs/2605.20101) · DTU | 3D 致动器拓扑、非线性 FEM 与打印件压力–弯曲测试 | 把任务目标和少量探测引入逐资产编辑 |
| 5 | [Function-Preserving Data Generation](https://arxiv.org/abs/2609.18293) · HKUST(GZ) | 网格变形时约束接触界面，在真实/模拟任务评价 | 加入可形变材料辨识与新受力工况 |
| 6 | [KnockGS](https://arxiv.org/abs/2608.27365) · Tuojing / Southeast | 已知施力校准弹性与密度，评价新力响应 | 从物性校准走到目标功能的局部几何编辑 |
| 7 | [MonoPhysics](https://arxiv.org/abs/2605.30320) · UNC Chapel Hill | 从单目视频联合恢复 3D 几何、外观与可形变物性 | 用主动探测与目标任务检验冻结后的资产 |
| 8 | [BendTwin](https://arxiv.org/abs/2608.06164) · Cambridge | 稀疏 RGB-D 重建含弯曲刚度与阻尼的弹簧质量模型 | 单独验证物性真值与新载荷响应 |
| 9 | [DiffPhD](https://arxiv.org/abs/2605.14526) · National Taiwan University / NUS / UBC 等 | 异质材料、接触与 3D 柔体轨迹的可微求解和梯度检查 | 接到生成资产与真实样品的功能评价 |
| 10 | [Warp-Geo](https://arxiv.org/abs/2609.20964) · Notre Dame | 可微 3D SDF 用于流固耦合及逆向形状优化 | 增加局部材料编辑与测试时预算协议 |
| 11 | [PhysX-Omni](https://arxiv.org/abs/2605.21572) · Nanyang Technological University | 生成刚体、柔体、关节可仿真资产及属性评价 | 在新载荷下独立测得功能响应 |
| 12 | [SNAP3D](https://arxiv.org/abs/2609.13146) · CMU | 单图部件的接触/连接修正、稳定性和打印装配 | 从装配几何扩展到内部物性与多种柔体功能 |

## 最值得细读的 5 篇

### 1. [PG-3DGS](https://arxiv.org/abs/2605.11266)：把物理目标写进 3D 表示的编辑

- **[事实]** 以 3D Gaussian 几何为变量，用可微的倾倒或升力目标优化形状，并报告 3D 打印飞机的升力测试。
- **[推断]** 它展示了“视觉 3D 资产 → 物理目标 → 几何修改 → 实物测量”的可行闭环；可形变材料场与未见载荷下的响应仍需单独建立。
- **精读重点：**物理损失如何传回 3DGS、几何合法性如何保持、真实测量与仿真目标怎样对齐。

### 2. [DeformSmith](https://arxiv.org/abs/2609.18620)：生成可形变资产时加入物理探针

- **[事实]** 从文本或单图构造几何和材料模型，以物理探针和仿真反馈调整资产，并报告操作任务评价。
- **[推断]** 这是本目录中生成可形变资产并引入仿真反馈的近邻；仍应核对它是否属于逐资产 TTT、是否同时优化局部几何与材料、操作成功是否进入每轮反馈、探针是否主动选择，以及真实材料/力学保真是否独立测量。
- **精读重点：**层级变量、每轮仿真预算、失败定位如何影响下一轮编辑，及其真实物体评价口径。

### 3. [KnockGS](https://arxiv.org/abs/2608.27365)：由已知作用力辨识隐藏物性

- **[事实]** 校准物理 Gaussian 的弹性和密度尺度，报告参数恢复及新方向、新强度作用力的响应评价。
- **[推断]** 这是已知受力校准模块的近邻；主动选择探针及夹持、弯曲等目标功能所需的几何/材料编辑仍待加入。
- **精读重点：**载荷是否真正已知、弹性和密度的可辨识性、冻结参数后的未见力误差。

### 4. [Towards end-to-end optimization in multimaterial 3D printing](https://arxiv.org/abs/2607.13174)：几何与材料共优化

- **[事实]** 用实验拟合的超弹性本构律、FEniCSx 和伴随方法优化结构拓扑及打印材料组分，包含夹爪接触应用。
- **[推断]** 提供“形状 + 材料”联合设计的力学核心；源材料尚不足以断言最终打印设计已实测证明功能增益。
- **精读重点：**离散材料可制造性、接触目标的梯度、材料标定误差怎样传到最终功能。

### 5. [DiffPhD](https://arxiv.org/abs/2605.14526)：支撑异质柔体与接触的可微求解

- **[事实]** 提供含异质材料与接触的可微投影动力学求解器，以 3D 四面体/FEM 任务和梯度检查评价。
- **[推断]** 可作为局部编辑后的物理反馈模块；仿真梯度正确不等于真实资产的功能可预测。
- **精读重点：**接触切换时梯度稳定性、网格/材料分辨率、内存和每次迭代成本。

## 100 篇目录

### 物性与动力学反演（25 篇）

| # | 论文与首发日 | 主要机构 | 物理变量或具体任务 | 评价方式 | 关联度 |
| ---: | --- | --- | --- | --- | --- |
| 1 | [CloDS: Visual-Only Unsupervised Cloth Dynamics Learning in Unknown Conditions](https://arxiv.org/abs/2602.01844)<br>2026-02-02 | [Renmin University of China](https://arxiv.org/html/2602.01844) | 未知物性条件下由多视角视频学习布料几何和动力学 | 多项实验及未见配置泛化 | 核心 |
| 2 | [MOSIV: Multi-Object System Identification from Videos](https://arxiv.org/abs/2603.06022)<br>2026-03-06 | [Carnegie Mellon University; Georgia Tech; Harvard University; ETH Zurich; UIUC; Insta360; UC Merced](https://arxiv.org/html/2603.06022) | 接触丰富视频中连续估计逐物体材料参数 | 新建合成多物体基准；参数 grounding 与长时仿真 | 核心 |
| 3 | [SLAT-Phys: Fast Material Property Field Prediction from Structured 3D Latents](https://arxiv.org/abs/2603.23973)<br>2026-03-25 | [University of Maryland, College Park](https://arxiv.org/html/2603.23973) | 由单张 RGB 预测体积杨氏模量、密度、泊松比 | 连续参数准确度和推理耗时，相比先前方法 | 核心 |
| 4 | [Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994)<br>2026-04-02 | [Xidian University](https://arxiv.org/html/2604.01994) | 3DGS 与 MPM 联合学习多种材料物理参数和动态响应（仿真参数联合优化，非独立真值辨识） | 合成与真实场景物理保真、运动一致性和 GPU 内存 | 核心 |
| 5 | [ReconPhys: Reconstruct Appearance and Physical Attributes from Single Video](https://arxiv.org/abs/2604.07882)<br>2026-04-09 | [GigaAI; Institute of Automation, Chinese Academy of Sciences](https://arxiv.org/html/2604.07882) | 单目视频联合预测非刚体几何、外观和物理属性 | 大规模合成数据；未来帧 PSNR 与 Chamfer 距离 | 核心 |
| 6 | [PhysHanDI: Physics-Based Reconstruction of Hand-Deformable Object Interactions](https://arxiv.org/abs/2605.09538)<br>2026-05-10 | [KAIST](https://arxiv.org/html/2605.09538) | 重建 3D 手和可变形物体，并以接触力驱动仿真 | 重建和未来预测，对比先前方法 | 相邻 |
| 7 | [MatPhys: Learning Material-Aware Physics Parameters for Deformable Object Simulation from Videos](https://arxiv.org/abs/2605.19386)<br>2026-05-19 | [The University of Osaka; Huawei Technologies Japan](https://arxiv.org/html/2605.19386) | 从单视角视频预测分部位 spring-mass 参数与材质嵌入 | 重建、未来预测、未见交互和物体泛化 | 核心 |
| 8 | [MoSA: Motion-constrained Stress Adaptation for Mitigating Real-to-Sim Gap in Continuum Dynamics via Learning Residual Anisotropy](https://arxiv.org/abs/2605.22597)<br>2026-05-21 | [HKUST Guangzhou; MMLab, The Chinese University of Hong Kong](https://arxiv.org/html/2605.22597) | 在各向同性仿真基线上学习各向异性与非均质残差应力 | 动态预测准确度、泛化与鲁棒性实验 | 核心 |
| 9 | [MonoPhysics: Estimating Geometry, Appearance, and Physical Parameters from Monocular Videos](https://arxiv.org/abs/2605.30320)<br>2026-05-28 | [University of North Carolina at Chapel Hill](https://arxiv.org/html/2605.30320) | 单目视频联合恢复 3D 几何、外观与可变形材料参数 | Vid2Sim 与新建弹塑性物体数据；和多视角基线比较 | 核心 |
| 10 | [SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image](https://arxiv.org/abs/2606.03994)<br>2026-06-02 | [Seoul National University](https://arxiv.org/html/2606.03994) | 借仿真诊断重建物体的形状、布局和支撑 | 物理稳定性和几何对齐基准 | 相邻 |
| 11 | [UniPixie: Unified and Probabilistic 3D Physics Learning via Flow Matching](https://arxiv.org/abs/2606.05399)<br>2026-06-03 | [University of Pennsylvania; Southern University of Science and Technology](https://arxiv.org/html/2606.05399) | 从视觉输入生成可模拟的材料属性分布，含杨氏模量 | PixieMultiverse；杨氏模量误差及跨 MPM/LBS/弹簧质量模型 | 核心 |
| 12 | [PhysAgent: Automating Physics-Based 4D Synthesis via Trajectory-Grounded Multi-Agent Feedback](https://arxiv.org/abs/2606.08688)<br>2026-06-07 | [Beijing Institute of Technology](https://arxiv.org/html/2606.08688) | 多 agent 在仿真回路中调整外力场与材料设置 | 场景多样性和物理准确度 | 相邻 |
| 13 | [EgoPhys: Learning Generalizable Physics Models of Deformable Objects from Egocentric Video](https://arxiv.org/abs/2606.16202)<br>2026-06-15 | [UC San Diego](https://arxiv.org/html/2606.16202) | 从第一视角 RGB 视频预测稠密弹簧刚度场 | 自建第一视角交互数据；重建、未来预测、零样本泛化；xArm6 演示 | 核心 |
| 14 | [Adaptive Volumetric Mechanical Property Fields Invariant to Resolution](https://arxiv.org/abs/2606.18231)<br>2026-06-16 | [NVIDIA; University of Toronto](https://arxiv.org/html/2606.18231) | 从 3D 资产预测空间变化的 E、泊松比和密度 | 属性场准确度、分辨率与测试时计算量 | 核心 |
| 15 | [One Video, One World: Turning Monocular Video into Physical 4D Scenes](https://arxiv.org/abs/2606.31388)<br>2026-06-30 | [Tsinghua University Shenzhen International Graduate School; SparcAI](https://arxiv.org/html/2606.31388) | 单目视频恢复逐实例拓扑、尺度、6DoF 和接触支撑 | 两组合成 benchmark；几何/布局/物理稳定性 | 相邻 |
| 16 | [BendTwin: Robust Dense-to-Sparse Physical Reconstruction with Bending-Aware Differentiable Spring-Mass Models](https://arxiv.org/abs/2608.06164)<br>2026-08-06 | [University of Cambridge](https://arxiv.org/html/2608.06164) | 从稀疏视角 RGB-D 重建含弯曲刚度及阻尼项的弹簧质量孪生 | 对比 PhysTwin；不同稀疏采样比的消融和未来预测 | 核心 |
| 17 | [Learning Implicit Constitutive Laws for Dynamic 3D Gaussian Splatting from Monocular Videos](https://arxiv.org/abs/2608.22102)<br>2026-08-22 | [The University of Hong Kong](https://arxiv.org/html/2608.22102) | 用静态多视角扫描初始化几何，再从单目动态视频学习隐式本构律 | 合成、real-to-sim、真实数据；Chamfer 和动态重建 | 核心 |
| 18 | [Gen2Physics: Grounding Generated 3D Meshes in Physics via Multi-View Material Decomposition](https://arxiv.org/abs/2608.23869)<br>2026-08-24 | [University of Bristol](https://arxiv.org/html/2608.23869) | 将生成 mesh 分区材料、推断内部空实与质量 | ABO-500、PartNet-Material；材质 mIoU 与质量估计 | 相邻 |
| 19 | [KnockGS: Interaction-Grounded Calibration of Physical Gaussian Representations](https://arxiv.org/abs/2608.27365)<br>2026-08-27 | [Tuojing Intelligence; Southeast University](https://arxiv.org/html/2608.27365) | 已知外力下校准物理 Gaussian 的弹性与密度尺度 | 五个 held-out 材料目标；参数恢复；新方向/强度作用力响应 | 核心 |
| 20 | [ChainSplat: A Physics-Inspired Screw-Theoretic Model for Learning Deformable Linear Object Dynamics from Multi-View RGB Videos](https://arxiv.org/abs/2608.28570)<br>2026-08-28 | [KTH Royal Institute of Technology](https://arxiv.org/html/2608.28570) | 从多视角 RGB 联合恢复线性可变形物体几何、状态和动力学 | 真实交互中的动态预测、3D 几何和 RGB 渲染 | 核心 |
| 21 | [PhysMAS: Physics-Grounded Multi-Agent Synthesis of Compositional 4D Gaussians](https://arxiv.org/abs/2609.07174)<br>2026-09-07 | [Beijing Institute of Technology](https://arxiv.org/pdf/2609.07174) | 多 agent 为多部位 4D Gaussian 分配材料并检查 MPM 配置 | 语义一致性、感知物理合理性与运行时间 | 相邻 |
| 22 | [RealSimLoop: Online Real-to-Sim Adaptation via Differentiable Reduced-Order Simulation with Vision Feedback](https://arxiv.org/abs/2609.09828)<br>2026-09-09 | [South China University of Technology](https://arxiv.org/html/2609.09828) | 用视觉反馈在线修正材料刚度，并恢复内应力和外力 | 离线基线比较；外力预测、3D 应力场、新视角合成 | 核心 |
| 23 | [SNAP3D: Physically Grounded 3D Parts for Assembly from a Single Image](https://arxiv.org/abs/2609.13146)<br>2026-09-11 | [Carnegie Mellon University](https://arxiv.org/html/2609.13146) | 单图分件 3D 生成后逆向修正接触图、连接器与稳定性 | 重力稳定性协议；3D 打印和真实装配 | 相邻 |
| 24 | [Wind on Trees: Testing Physical Grounding in Dynamic 4D Gaussian Splatting](https://arxiv.org/abs/2609.17810)<br>2026-09-15 | [University of Alberta](https://arxiv.org/html/2609.17810) | 风驱树木视频拟合部位振子频率和阻尼 | 受控合成树；留出视角、时间外推、未见风速、参数恢复；摘要报告阻尼恢复失败 | 核心 |
| 25 | [PhysVGGT: Feed-Forward Dense Physical Property Estimation from A Single Image](https://arxiv.org/abs/2609.18920)<br>2026-09-16 | [Huawei Noah's Ark Lab; Concordia University](https://arxiv.org/html/2609.18920) | 逐像素预测摩擦、Shore 硬度、杨氏模量、密度及物体质量 | ABO-500 与域外 NeRF2Physics；速度 0.13 秒/图 | 相邻 |

### 可交互物理场景与资产（29 篇）

| # | 论文与首发日 | 主要机构 | 物理变量或具体任务 | 评价方式 | 关联度 |
| ---: | --- | --- | --- | --- | --- |
| 26 | [MotionPhysics: Learnable Motion Distillation for Text-Guided Simulation](https://arxiv.org/abs/2601.00504)<br>2026-01-01 | [University of Edinburgh](https://arxiv.org/pdf/2601.00504) | 材料参数；弹性体、金属、泡沫、沙和流体动力学 | 超过 30 个真实、设计或生成的 3D 场景；比较运动真实感 | 核心 |
| 27 | [ReWeaver: Towards Simulation-Ready and Topology-Accurate Garment Reconstruction](https://arxiv.org/abs/2601.16672)<br>2026-01-23 | [Zhejiang University; Shanghai Innovation Institute; Westlake University](https://arxiv.org/html/2601.16672) | 服装拓扑、接缝与网格裁片 | 拓扑及几何重建，并检查下游布料仿真的可用性 | 相邻 |
| 28 | [FastPhysGS: Accelerating Physics-based Dynamic 3DGS Simulation via Interior Completion and Adaptive Optimization](https://arxiv.org/abs/2602.01723)<br>2026-02-02 | [Sun Yat-sen University](https://arxiv.org/html/2602.01723) | 重建物体的材料参数与 MPM 形变 | 与既有物理 3DGS 方法比较仿真保真度、运行时间和内存 | 核心 |
| 29 | [i-PhysGaussian: Implicit Physical Simulation for 3D Gaussian Splatting](https://arxiv.org/abs/2602.17117)<br>2026-02-19 | [University of Sydney](https://arxiv.org/html/2602.17117) | 应力、动量平衡及高刚度或准静态形变 | 与显式积分器比较时间步稳定性和结构连贯性 | 核心 |
| 30 | [Phys4D: Fine-Grained Physics-Consistent 4D Modeling from Video Diffusion](https://arxiv.org/abs/2603.03485)<br>2026-03-03 | [Northwestern University](https://arxiv.org/pdf/2603.03485) | 生成 4D 序列的 3D 几何、运动与接触一致性 | 基于仿真数据训练，评价几何与运动一致性 | 相邻 |
| 31 | [RealWonder: Real-Time Physical Action-Conditioned Video Generation](https://arxiv.org/abs/2603.05449)<br>2026-03-05 | [Stanford University](https://arxiv.org/html/2603.05449) | 受 3D 外力条件约束的场景动力学与材料先验 | 交互式视频生成、作者演示及物理动作条件控制 | 相邻 |
| 32 | [DiffWind: Physics-Informed Differentiable Modeling of Wind-Driven Object Dynamics](https://arxiv.org/abs/2603.09668)<br>2026-03-10 | [Zhejiang University, State Key Laboratory of CAD & CG](https://arxiv.org/pdf/2603.09668) | 时空风力场与可形变物体动力学 | WD-Objects 合成和真实场景；新风力下的仿真保真度 | 核心 |
| 33 | [Zero-Shot Reconstruction of Animatable 3D Avatars with Cloth Dynamics from a Single Image](https://arxiv.org/abs/2603.14772)<br>2026-03-16 | [Korea University](https://arxiv.org/pdf/2603.14772) | 身体运动下的布料表观形变 | 动态捕捉数据集上的视觉动画质量 | 相邻 |
| 34 | [PhysHead: Simulation-Ready Gaussian Head Avatars](https://arxiv.org/abs/2604.06467)<br>2026-04-07 | [Max Planck Institute for Intelligent Systems](https://arxiv.org/html/2604.06467) | 风作用下的发丝动力学 | 虚拟人定量及定性比较，并测试仿真风响应 | 核心 |
| 35 | [PhysInOne: Visual Physics Learning and Reasoning in One Suite](https://arxiv.org/abs/2604.09415)<br>2026-04-10 | [vLAR Group, Hong Kong Polytechnic University](https://arxiv.org/html/2604.09415) | 力学、光学、流体与磁学属性标签 | 物理感知生成、未来预测和属性估计等四项任务 | 核心 |
| 36 | [PhysForge: Generating Physics-Grounded 3D Assets for Interactive Virtual World](https://arxiv.org/abs/2605.05163)<br>2026-05-06 | [University of Hong Kong; Tencent Hunyuan](https://arxiv.org/pdf/2605.05163) | 部件结构、关节及运动学性质与物理属性 | 生成的交互资产质量；具体仿真器验证指标未核实 | 核心 |
| 37 | [FLUIDSPLAT: Reconstructing Physical Fields from Sparse Sensors via Gaussian Primitives](https://arxiv.org/abs/2605.18866)<br>2026-05-15 | [Shanghai AI Laboratory](https://arxiv.org/html/2605.18866) | 从稀疏表面传感器估计连续 2D/3D 流场 | 圆柱、AirfRANS、FlowBench LDC-3D 和 PhySense-Car 的 3D 场误差 | 核心 |
| 38 | [PhysOmni: Physics-Grounded Multi-Object Scene Generation from a Single Image with Real-Time Interaction](https://arxiv.org/abs/2605.20290)<br>2026-05-19 | [Fudan University; TeleAI, China Telecom](https://arxiv.org/html/2605.20290) | 多物体材料、刚体及柔体动力学与接触 | 交互成功率、穿透量和实时预览；数值需回查原文 | 核心 |
| 39 | [PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects](https://arxiv.org/abs/2605.21572)<br>2026-05-20 | [Nanyang Technological University, S-Lab](https://arxiv.org/html/2605.21572) | 刚体、柔体和关节资产的几何与属性 | PhysX-Bench 的六个维度，涵盖结构、外观和物理属性 | 核心 |
| 40 | [Physics-Aware 3D Gaussian Editing for Driving Scene Generation](https://arxiv.org/abs/2605.25373)<br>2026-05-25 | [Jilin University](https://arxiv.org/html/2605.25373) | 道路纵断面及车辆垂向位移和俯仰响应 | Waymo 场景编辑；视觉一致性与运行时间；未报告真实车辆物理验证 | 核心 |
| 41 | [REST3D: Reconstructing Physically Stable 3D Scenes from a Single Image](https://arxiv.org/abs/2605.30338)<br>2026-05-28 | [Carnegie Mellon University](https://arxiv.org/pdf/2605.30338) | 物体支撑及接触关系与重力下稳定放置 | 交互仿真中的沉降与场景重建测试 | 核心 |
| 42 | [PhyGenHOI: Physically-Aware 4D Generation of Dynamic Human-Object Interactions](https://arxiv.org/abs/2605.30268)<br>2026-05-28 | [Hebrew University of Jerusalem](https://arxiv.org/pdf/2605.30268) | 接触冲量、动量传递与物体形变 | 跨动作和物体评价生成的 4D 人物交互物理一致性 | 核心 |
| 43 | [CA-World: Multi-Object Counterfactual Alignment for Efficient Interactive-Ready Reconstruction](https://arxiv.org/abs/2605.30239)<br>2026-05-28 | [Tsinghua University, Shenzhen International Graduate School](https://arxiv.org/pdf/2605.30239) | 完整物体几何、接触放置和可交互场景状态 | 多物体仿真就绪度；当前版本的具体指标待核实 | 相邻 |
| 44 | [FreeForm: Reduced-Order Deformable Simulation from Particle-Based Skinning Eigenmodes](https://arxiv.org/abs/2605.29318)<br>2026-05-28 | [NVIDIA Research](https://arxiv.org/html/2605.29318) | 降阶弹性形变模态 | 相对神经场的仿真误差和速度；具体条件需查论文 | 核心 |
| 45 | [Perceptual 3D Simulation With Physical World Modeling](https://arxiv.org/abs/2606.27575)<br>2026-06-25 | [Stanford University](https://arxiv.org/html/2606.27575) | 概率化 3D 场景状态及变换作用 | 部分可观测条件下的未来 3D 场景预测；具体指标未核实 | 核心 |
| 46 | [UniPhysGen: Unified Physical Grounding for Simulation-Ready 3D Assets](https://arxiv.org/abs/2607.13586)<br>2026-07-15 | [Zhejiang University](https://arxiv.org/html/2607.13586) | 部件物理语义、关节轴、物体尺度和质量 | UniPhys-Bench 的 1,927 个物体；属性与关节预测，以及流水线仿真检查 | 核心 |
| 47 | [LaGSplat: Inferring Physics-Governed Interactive Simulation from Monocular Video Using Latent Lagrangian Gaussian Splatting](https://arxiv.org/abs/2608.16324)<br>2026-08-17 | [CEA LIST; Université Paris-Saclay](https://arxiv.org/html/2608.16324) | 广义坐标、耗散与外力响应 | 刚体到柔体测试；单目视频与传感器测量；未见外力响应 | 核心 |
| 48 | [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212)<br>2026-08-25 | [Shanghai Jiao Tong University](https://arxiv.org/html/2608.24212) | 生成场景中的质量、碰撞、支撑关系和关节运动 | 物理引擎反馈；稳定堆叠及交互演示 | 核心 |
| 49 | [MeshPriorDiT: Hierarchical Modeling for Action-Conditioned Cloth Dynamics](https://arxiv.org/abs/2608.26766)<br>2026-08-27 | [Tsinghua University](https://arxiv.org/pdf/2608.26766) | 布料顶点位移与边缘应变 | 三项布料任务；15 步预测的全局均方误差和边缘应变均方误差 | 核心 |
| 50 | [SceneMosaic: Efficient and Diverse Simulation-Ready Scene Generation via Hybrid Agentic Layout Evolution](https://arxiv.org/abs/2609.05594)<br>2026-09-04 | [University of Hong Kong](https://arxiv.org/pdf/2609.05594) | 物体布局、支撑关系和稳定性合理度 | SceneEval-100 的语义与布局评价，以及报告的 24 倍运行速度提升 | 相邻 |
| 51 | [TourPhysics: Bringing Physics to World Models for Exploration and Manipulation from a Single Image](https://arxiv.org/abs/2609.04911)<br>2026-09-04 | [Fudan University; TeleAI, China Telecom](https://arxiv.org/html/2609.04911) | 物体运动、接触与可形变干预 | 探索及操作演示；物理与视频一致性的数值指标未核实 | 核心 |
| 52 | [DeformSmith: Physics Harness-Guided Hierarchical Generation of Deformable Assets for Robot Manipulation](https://arxiv.org/abs/2609.18620)<br>2026-09-16 | [Nankai University](https://arxiv.org/html/2609.18620) | 生成资产的可形变材料属性与稳定性 | 仿真探针与操作成功率；真实世界保真度需回查原文 | 核心 |
| 53 | [SplashSplat: Reconstructing Splashing Liquids from Real-World Multi-View Videos](https://arxiv.org/abs/2609.20818)<br>2026-09-17 | [EPFL](https://arxiv.org/pdf/2609.20818) | 液面界面及粗尺度速度输运 | 七台同步 4K 相机、20 个场景；评价渲染与运动合理性 | 核心 |
| 54 | [φ-RIE: From Photorealistic Reconstruction to Interactive Environments](https://arxiv.org/abs/2609.26795)<br>2026-09-22 | [INSAIT, Sofia University](https://arxiv.org/html/2609.26795) | 可移动资产、碰撞及接触几何和被遮挡环境 | 50 个 ScanNet++ 场景；资产可执行性及操作增益 | 核心 |

### 可形变资产与材料功能编辑（15 篇）

| # | 论文与首发日 | 主要机构 | 物理变量或具体任务 | 评价方式 | 关联度 |
| ---: | --- | --- | --- | --- | --- |
| 55 | [EMPM: Embodied MPM for Modeling and Simulation of Deformable Objects](https://arxiv.org/abs/2601.17251)<br>2026-01-24 | [Robotics and AI Institute](https://arxiv.org/html/2601.17251) | 3D几何/外观、MPM材料参数和变形状态 | 多视角RGB-D重模拟误差；与弹簧质量基线比较；在线传感反馈更新 | 核心 |
| 56 | [SoMA: A Real-to-Sim Neural Simulator for Robotic Soft-body Manipulation](https://arxiv.org/abs/2602.02402)<br>2026-02-02 | [Fudan University; Shanghai AI Laboratory](https://arxiv.org/html/2602.02402) | 3D Gaussian软体状态、环境力、机器人关节动作 | 真实机器人软体操作重模拟、未见轨迹泛化和长程布料折叠 | 核心 |
| 57 | [Generalized Task-Driven Design of Soft Robots via Reduced-Order FEM-based Surrogate Modeling](https://arxiv.org/abs/2603.19794)<br>2026-03-20 | [University of Oxford, Oxford Robotics Institute](https://arxiv.org/html/2603.19794) | 软致动器参数、降阶FEM响应、3D形状和夹爪设计 | 跨致动器sim-to-real；软夹爪RL协同设计；3D致动器形状匹配 | 核心 |
| 58 | [FluidGaussian: Propagating Simulation-Based Uncertainty Toward Functionally-Intelligent 3D Reconstruction](https://arxiv.org/abs/2603.21356)<br>2026-03-22 | [Simon Fraser University](https://arxiv.org/html/2603.21356) | 3D表面几何、流场速度散度及仿真不确定性 | NeRF Synthetic、Mip-NeRF 360、DrivAerNet++的PSNR和流场速度散度 | 核心 |
| 59 | [MAVEN: A Mesh-Aware Volumetric Encoding Network for Simulating 3D Flexible Deformation](https://arxiv.org/abs/2604.04474)<br>2026-04-06 | [Peking University; University of Southampton](https://arxiv.org/html/2604.04474) | 以单元、面片和顶点编码的形变状态 | 网格感知体积神经仿真器；柔性及接触数据集与金属拉伸弯曲任务 | 相邻 |
| 60 | [SIM1: Physics-Aligned Simulator as Zero-Shot Data Scaler in Deformable Worlds](https://arxiv.org/abs/2604.08544)<br>2026-04-09 | [Shanghai AI Laboratory](https://arxiv.org/html/2604.08544) | 场景尺度、弹性动力学、接触/布料轨迹 | 真实机器人零样本布料操作；摘要报告90%成功率与50%泛化提升 | 核心 |
| 61 | [i-Tac: Inverse Design of 3D-Printed Tactile Elastomers with Scalable and Tunable Optical and Mechanical Properties](https://arxiv.org/abs/2604.10692)<br>2026-04-12 | [Imperial College London](https://arxiv.org/pdf/2604.10692) | 面向目标硬度与透明度的树脂配比 | 响应面优化后打印弹性体，并测试其光学与力学性质 | 相邻 |
| 62 | [DiffPhD: A Unified Differentiable Solver for Projective Heterogeneous Materials in Elastodynamics with Contact-Rich GPU-Acceleration](https://arxiv.org/abs/2605.14526)<br>2026-05-14 | [National Taiwan University; National University of Singapore; University of British Columbia; National Yang Ming Chiao Tung University; MoonShine Animation Studio](https://arxiv.org/html/2605.14526) | 非均质刚度及材料状态与可形变轨迹 | 可微投影动力学接触求解器；3D 四面体及 FEM 基准与梯度检查 | 相邻 |
| 63 | [PIAvatar: Physically Interactive Avatars via Deformation Gradient Decoupling](https://arxiv.org/abs/2606.21162)<br>2026-06-19 | [GIST; KETI; Polygom; Chung-Ang University (collective author line)](https://arxiv.org/html/2606.21162) | 形变梯度、运动学速度、MPM应力和接触响应 | 人-物/人-人接触与形变场景评价 | 核心 |
| 64 | [Scene-Level Heterogeneous Physics Simulation with 3D Gaussian Splats](https://arxiv.org/abs/2606.21753)<br>2026-06-19 | [University of Hong Kong](https://arxiv.org/html/2606.21753) | 可形变3DGS、网格、流体粒子与静态碰撞边界 | 场景级双向交互/碰撞及异质求解器演示 | 核心 |
| 65 | [DeformX: A Versatile Co-Simulation Framework for Deformable Linear Objects](https://arxiv.org/abs/2606.22116)<br>2026-06-20 | [Carnegie Mellon University, Robotics Institute](https://arxiv.org/html/2606.22116) | Cosserat杆弯曲/扭转/剪切、自碰撞及网格接触 | 真实实验物理/视觉一致性；UR5e绳摆任务目标误差 | 核心 |
| 66 | [MeGAS: Thermomechanical Dynamic Gaussian Splatting for Thermophysical Scene Editing](https://arxiv.org/abs/2606.23455)<br>2026-06-22 | [State Key Laboratory of CAD&CG, Zhejiang University; University of British Columbia](https://arxiv.org/html/2606.23455) | 逐 Gaussian 温度及热力耦合相态和状态 | 热对流扩散与 MPM 相变动力学，以及渲染场景 | 核心 |
| 67 | [Contact-based inverse analysis for nonlinear material identification in spatially heterogeneous solids](https://arxiv.org/abs/2607.18156)<br>2026-07-20 | [Gdańsk University of Technology; Ruhr University Bochum; Indian Institute of Technology Guwahati](https://arxiv.org/pdf/2607.18156) | 空间变化的非线性超弹性材料参数 | 利用压痕位移及接触力进行等几何有限元模型更新；3D 块体和壳体实例 | 核心 |
| 68 | [Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents](https://arxiv.org/abs/2607.19190)<br>2026-07-21 | [University of British Columbia; National University of Singapore](https://arxiv.org/html/2607.19190) | 场景几何、物体状态、物理参数、机器人轨迹和可执行episode | 刚体/变形交互/人形场景转换；策略微调和真实策略代理评价 | 核心 |
| 69 | [Function-Preserving Data Generation for Zero-Shot Real-to-Sim-to-Real Manipulation](https://arxiv.org/abs/2609.18293)<br>2026-09-16 | [Hong Kong University of Science and Technology (Guangzhou)](https://arxiv.org/html/2609.18293) | 约束引导网格变形、接触界面、任务位姿和碰撞代理 | 真实和模拟接触丰富任务上的零样本策略泛化 | 核心 |

### 结构、接触与流体逆向设计（23 篇）

| # | 论文与首发日 | 主要机构 | 物理变量或具体任务 | 评价方式 | 关联度 |
| ---: | --- | --- | --- | --- | --- |
| 70 | [Stress-constrained Topology Optimization for Metamaterial Microstructure Design](https://arxiv.org/abs/2602.19662)<br>2026-02-23 | [Arts et Métiers Institute of Technology; CNRS; CNAM](https://arxiv.org/html/2602.19662) | 3D 超材料密度场 | 包含循环载荷的应力约束有限元评价 | 核心 |
| 71 | [TurboAgent: An LLM-Driven Autonomous Multi-Agent Framework for Turbomachinery Aerodynamic Design](https://arxiv.org/abs/2604.06747)<br>2026-04-08 | [Chinese Academy of Sciences, Institute of Engineering Thermophysics; University of Chinese Academy of Sciences](https://arxiv.org/pdf/2604.06747) | 压缩机叶片几何 | 高保真跨音速 CFD | 核心 |
| 72 | [Topology Optimization for Materially Efficient Reinforced Concrete Design: Development, Fabrication, and Structural Evaluation](https://arxiv.org/abs/2604.22070)<br>2026-04-23 | [Massachusetts Institute of Technology](https://arxiv.org/pdf/2604.22070) | 钢筋混凝土梁拓扑 | 制作样件并进行机械载荷测试 | 核心 |
| 73 | [Inverse Design of Cellular Composites for Targeted Nonlinear Mechanical Response via Multi-Fidelity Bayesian Optimisation](https://arxiv.org/abs/2604.26657)<br>2026-04-29 | [Queen Mary University of London](https://arxiv.org/html/2604.26657) | 3D Spinodoid 单胞设计 | 非线性 FEM 与压缩实验 | 核心 |
| 74 | [Geometry-Aware Neural Optimizer for Shape Optimization and Inversion](https://arxiv.org/abs/2605.04474)<br>2026-05-06 | [Renmin University of China](https://arxiv.org/html/2605.04474) | 3D 车辆表面形状 | 几何场神经代理模型及风阻比较 | 核心 |
| 75 | [Inverse Design of Metainterfaces for Static Friction Control: Beyond the Hertzian Limit](https://arxiv.org/abs/2605.11012)<br>2026-05-10 | [École Polytechnique Fédérale de Lausanne](https://arxiv.org/html/2605.11012) | 微凸体表面形貌及接触定律 | 可微接触力学与独立边界元法校验 | 核心 |
| 76 | [PG-3DGS: Optimizing 3D Gaussian Splatting to Satisfy Physics Objectives](https://arxiv.org/abs/2605.11266)<br>2026-05-11 | [Purdue University](https://arxiv.org/html/2605.11266) | 3D Gaussian 几何 | 可微倒液及升力物理目标，并实测打印飞机的升力 | 核心 |
| 77 | [Topology-Optimized Pneumatic Soft Actuator: Design and Experimental Validation](https://arxiv.org/abs/2605.20101)<br>2026-05-19 | [Technical University of Denmark](https://arxiv.org/pdf/2605.20101) | 3D 致动器材料拓扑 | 非线性孔弹性超弹性 FEM，以及制造样件的气压弯曲测试 | 核心 |
| 78 | [Adaptive Multi-Fidelity Structural Optimization under Fluid-Structure Interaction](https://arxiv.org/abs/2605.20501)<br>2026-05-19 | [Virginia Tech; University of British Columbia](https://arxiv.org/html/2605.20501) | 流固耦合中的结构几何 | 以高保真耦合 FSI 进行最终评价 | 核心 |
| 79 | [TO-Agents: A Multi-Agent AI Framework for Subjective Preference-Guided Topology Optimization](https://arxiv.org/abs/2605.21622)<br>2026-05-20 | [Massachusetts Institute of Technology](https://arxiv.org/pdf/2605.21622) | 3D 拓扑优化求解器参数 | 确定性拓扑优化求解器，以及偏好和可制造性评估 | 相邻 |
| 80 | [ShapeBench: A Scalable Benchmark and Diagnostic Suite for Standardized Evaluation in Aerodynamic Shape Optimization](https://arxiv.org/abs/2605.20763)<br>2026-05-20 | [Stanford University](https://arxiv.org/html/2605.20763) | 103 项任务中的气动外形 | 经验证的代理模型；条件允许时采用高保真 CFD | 相邻 |
| 81 | [Unfrustrated Self-Morphing of Bulk Liquid Crystal Elastomers](https://arxiv.org/abs/2605.25187)<br>2026-05-24 | [Weizmann Institute of Science; Tel Aviv University](https://arxiv.org/html/2605.25187) | 三维块体向列相指向矢场 | 解析几何相容性与弹性应力理论 | 相邻 |
| 82 | [Shape optimization of pneumatic soft actuators](https://arxiv.org/abs/2606.30800)<br>2026-06-29 | [Harvard University; Lund University](https://arxiv.org/html/2606.30800) | 3D 气动致动器边界 | 非线性力学响应的梯度优化 | 核心 |
| 83 | [TO-Master: an LLM-agent framework for automated topology optimization](https://arxiv.org/abs/2607.01812)<br>2026-07-02 | [Hong Kong University of Science and Technology](https://arxiv.org/html/2607.01812) | 3D 结构密度场和 FEM 设置 | 基于 FEM 的柔度及应力优化 | 核心 |
| 84 | [Towards end-to-end optimization in multimaterial 3D printing](https://arxiv.org/abs/2607.13174)<br>2026-07-14 | [Cornell University](https://arxiv.org/html/2607.13174) | 拓扑与打印材料组分 | 实验拟合的超弹性本构，结合 FEniCSx 伴随法 | 核心 |
| 85 | [A Generalized Shape Function Approach for Multimaterial Topology Optimization](https://arxiv.org/abs/2607.20784)<br>2026-07-22 | [Indian Institute of Technology Hyderabad](https://arxiv.org/pdf/2607.20784) | 3D 多材料密度场 | FEM 刚度与柔顺机构目标 | 核心 |
| 86 | [∂²(TO): A Dual Topological Derivative-Based Enriched Topology Optimization for Fracture Mitigation in 3-D Brittle Solids](https://arxiv.org/abs/2607.23525)<br>2026-07-26 | [Delft University of Technology](https://arxiv.org/pdf/2607.23525) | 3D 脆性固体的水平集形状 | 增广 FEM 的能量释放率 | 核心 |
| 87 | [Instability-induced bistable shape-morphing kirigami structures](https://arxiv.org/abs/2607.26941)<br>2026-07-29 | [University of Edinburgh](https://arxiv.org/html/2607.26941) | 面向目标 3D 形状的剪纸切口 | 力学模型、FEM 与实体实验 | 核心 |
| 88 | [Machine-learning-assisted multiscale topology optimization of functionally graded superimposed lattice structures](https://arxiv.org/abs/2608.28513)<br>2026-08-28 | [Indian Institute of Technology Roorkee](https://arxiv.org/html/2608.28513) | 3D BCC/FCC/SC 晶格单胞参数 | 均匀化及 FEM 与 3D MBB 梁评价 | 核心 |
| 89 | [HGTO: A Unified Graph-Based Physics-Informed Formulation for Structural Topology Optimization](https://arxiv.org/abs/2609.15001)<br>2026-09-14 | [Arizona State University](https://arxiv.org/html/2609.15001) | 3D 结构密度场 | 包含弹塑性的可微 FEM 平衡 | 核心 |
| 90 | [Warp-Geo: Differentiable Geometry Representation for Dynamic-Boundary Simulation and Shape Optimization](https://arxiv.org/abs/2609.20964)<br>2026-09-17 | [University of Notre Dame](https://arxiv.org/html/2609.20964) | 3D SDF 几何与形状 | 可微 FSI 和逆向优化；梯度检查 | 核心 |
| 91 | [KATOsuper: Surrogate-accelerated neural topology optimization with sensitivity-consistent Fourier neural operators](https://arxiv.org/abs/2609.27216)<br>2026-09-23 | [University of British Columbia](https://arxiv.org/pdf/2609.27216) | 3D 拓扑密度场 | 3D 柔度及应力 FEA 基准 | 核心 |
| 92 | [Growth-Inspired Graph Generation and Inverse Design of Mechanical Lattices via Dot Matrices Database Augmentation and GCNN](https://arxiv.org/abs/2609.29024)<br>2026-09-24 | [University of Illinois Urbana-Champaign](https://arxiv.org/pdf/2609.29024) | 3D 力学晶格图 | 基于梁单元的 FEM 刚度验证 | 核心 |

### 求解器、神经算子与基准（8 篇）

| # | 论文与首发日 | 主要机构 | 物理变量或具体任务 | 评价方式 | 关联度 |
| ---: | --- | --- | --- | --- | --- |
| 93 | [An open-source computational framework for immersed fluid-structure interaction modeling using FEBio and MFEM](https://arxiv.org/abs/2601.08266)<br>2026-01-13 | [University of Pennsylvania; Children's Hospital of Philadelphia; University of Utah](https://arxiv.org/html/2601.08266) | 流体速度及压力与超弹性或黏弹性固体形变 | 浸入式 FSI 测试，包括 3D 半月瓣心脏瓣膜 | 核心 |
| 94 | [FEM-Informed Hypergraph Neural Networks for Efficient Elastoplasticity](https://arxiv.org/abs/2602.07364)<br>2026-02-07 | [Hong Kong University of Science and Technology](https://arxiv.org/pdf/2602.07364) | 循环载荷下的 3D 位移、应变、应力与硬化 | 3D 弹塑性基准，对比 PINN 和 FEM 实现 | 核心 |
| 95 | [Smoothly Differentiable and Efficiently Vectorizable Contact Manifold Generation](https://arxiv.org/abs/2602.20304)<br>2026-02-23 | [EPFL; University of Tübingen; Idiap Research Institute](https://arxiv.org/html/2602.20304) | 带符号接触距离、法向量与接触流形点 | 相对 MuJoCo XLA 的碰撞例程速度及基础接触测试 | 核心 |
| 96 | [Four-field mixed finite elements for incompressible nonlinear elasticity](https://arxiv.org/abs/2603.08992)<br>2026-03-09 | [Monash University](https://arxiv.org/pdf/2603.08992) | 位移、形变梯度、Piola 应力和压力 | 2D/3D 收敛率及相对四场 FEM 的稳健性 | 核心 |
| 97 | [Spectrally Safe Neural Operator Warm-Starts for Large-Scale Newton Solvers](https://arxiv.org/abs/2606.21828)<br>2026-06-20 | [Brown University](https://arxiv.org/pdf/2606.21828) | 3D 超弹性位移、形变梯度行列式 det(F) 与雅可比特征值 | 640 万自由度 3D 弹性问题上的牛顿法收敛 | 核心 |
| 98 | [Differentiate the Solver, Not the Equation: Reverse-Sweep Adjoints for Block Implicit Simulation](https://arxiv.org/abs/2608.08559)<br>2026-08-09 | [Stanford University; UCLA; Tencent LightSpeed Studios; University of Utah](https://arxiv.org/html/2608.08559) | 3D 软体顶点状态、接触力与伴随梯度 | 梯度与展开式自动微分的一致性，以及 800 万顶点时的速度及内存 | 核心 |
| 99 | [PhysicsBench: A Unified Leaderboard for Generative and Predictive Models in Engineering Design and Simulation](https://arxiv.org/abs/2608.24056)<br>2026-08-25 | [KAIST; Narnia Labs](https://arxiv.org/pdf/2608.24056) | CAD 几何、CFD/FEA 场与工程标量目标 | 九个数据集上的 66 个模型，包括 3D 工业 CAD/CFD/FEA | 核心 |
| 100 | [Ostrich: Taking Large Strides Through Stiff Contact in Differentiable Dynamics](https://arxiv.org/abs/2609.08800)<br>2026-09-08 | [Czech Technical University in Prague](https://arxiv.org/html/2609.08800) | 刚体接触冲量、摩擦与轨迹梯度 | 真实机器人轨迹匹配、优化收敛及 GPU 吞吐量 | 核心 |

## 从这 100 篇看到的五个研究趋势

以下是这份**定向筛选目录内**的定性归纳，不是全领域论文数量趋势。

1. **视觉先验用于预测空间物性。** [SLAT-Phys](https://arxiv.org/abs/2603.23973)、[PhysVGGT](https://arxiv.org/abs/2609.18920) 从图像给出模量、密度、摩擦等预测，[UniPixie](https://arxiv.org/abs/2606.05399) 进一步表征材料分布。视觉预测可作为初始化；缺少已知受力时，真实物性仍可能有多解。
2. **部分工作以受力响应校准或评价。** [KnockGS](https://arxiv.org/abs/2608.27365) 用已知作用力校准并测试未见力；[BendTwin](https://arxiv.org/abs/2608.06164)、[MonoPhysics](https://arxiv.org/abs/2605.30320) 从动态观测建立可仿真模型。应分别报告参数真值误差与冻结后的响应误差。
3. **生成和编辑开始纳入物理目标。** [PhysX-Omni](https://arxiv.org/abs/2605.21572) 构造可仿真资产，[DeformSmith](https://arxiv.org/abs/2609.18620) 将物理探针放进生成循环，[PG-3DGS](https://arxiv.org/abs/2605.11266) 将功能目标直接用于几何优化。可导入仿真器与未见工况下可用是两级评价。
4. **几何、材料和接触已有各自的可微部件。** [Cornell 多材料打印工作](https://arxiv.org/abs/2607.13174) 优化拓扑与组分；[DiffPhD](https://arxiv.org/abs/2605.14526)、[可微接触流形](https://arxiv.org/abs/2602.20304) 和 [Warp-Geo](https://arxiv.org/abs/2609.20964) 提供求解或梯度部件。关键还在于把这几类变量接到**同一给定资产**的测试时编辑协议。
5. **部分工作报告制造后的功能测量。** [DTU 气动软致动器](https://arxiv.org/abs/2605.20101) 和 [PG-3DGS](https://arxiv.org/abs/2605.11266) 含制造后的力学测试，[PhysicsBench](https://arxiv.org/abs/2608.24056) 提供工程设计/仿真基准。目录内尚未看到可直接横向比较“少量探测—局部编辑—未见载荷功能”的统一协议。

## 10 篇适合做低算力机制实验的论文

以下均为**研究建议 `[推断]`**，不是论文已经报告的实验，也不代表原论文能以低算力完整复现。以冻结现成重建/生成模型、使用小规模 3D 网格和有限仿真预算为起点；每个提议都应报告实测 GPU 小时或 CPU 时间。三条分别给出改法、最小验证与预期收益/风险。

### 1. [SLAT-Phys](https://arxiv.org/abs/2603.23973)：把单图物性预测变成可校准先验

1. **区域置信度。** 将逐体素模量/密度压成少量区域参数及不确定区间；在合成异质块体上检验区间覆盖率。能降低优化维度，风险是细窄软层被区域化抹掉。
2. **主动压痕。** 从几个候选施力点选择最能区分材料假设的一个，与固定中心压痕比较未见载荷曲线。可能减少实测次数，风险是依赖可靠的力传感与接触定位。
3. **冻结视觉先验后的局部更新。** 只更新观测能约束的材料区域，和全场更新比较测试工况误差及过拟合。可抑制无依据改动，风险是错误的初始分区限制上限。

### 2. [BendTwin](https://arxiv.org/abs/2608.06164)：区分弯曲刚度与阻尼

1. **两种激励。** 用慢速加载和释放后的自由振动分别约束刚度、阻尼；小梁合成数据比较参数误差。可缓解参数耦合，风险是观测帧率不足。
2. **稀疏视角选择。** 固定两台 RGB-D 相机，比较覆盖最大曲率处与均匀布置的未来帧预测。可测试观测设计的价值，风险是遮挡改变结论。
3. **未见载荷协议。** 在相同拟合损失下，单独报告新作用点的力–位移曲线。能检验模型是否学到可迁移物性，风险是弹簧模型难表达局部屈曲。

### 3. [KnockGS](https://arxiv.org/abs/2608.27365)：让受力校准更可辨识

1. **选择施力方向。** 用候选材料对探测响应的分歧选择下一次施力；与随机、固定方向在相同次数下比较新力预测。潜在收益是少探测，风险是仿真先验偏差。
2. **几何–刚度解耦。** 固定物体外形或仅允许低维形变，对照几何与弹性同时自由优化时的参数恢复。可揭示互相代偿，风险是固定了错误几何。
3. **接触外推。** 在未见接触点、力幅值与方向的交叉组合上评价，不用校准探针选最优模型。能发现过拟合，风险是接触定位噪声主导误差。

### 4. [Function-Preserving Data Generation](https://arxiv.org/abs/2609.18293)：将接触功能约束加入 3D 编辑

1. **接触斑块不变量。** 在网格编辑时约束局部法向、面积与间隙，对照仅约束轮廓的夹持成功率。可能保持可用接触，风险是限制形状搜索空间。
2. **材料小扰动。** 在接触几何固定时改变 2–3 个区域刚度，用粗网格 FEM 看功能是否变化。可分离几何和材料作用，风险是接触摩擦未标定。
3. **独立求解器复核。** 用第二套接触求解设置评估筛出的几何，报告穿透和力峰差异。能筛掉求解器漏洞，风险是求解器间模型假设不同。

### 5. [PG-3DGS](https://arxiv.org/abs/2605.11266)：把功能编辑限制在可制造子空间

1. **低维局部形变。** 冻结 3DGS 外观，只调 5–20 个形状控制点，并与全局更新比较目标值和轮廓保持。可降低预算，风险是无法表达必要拓扑改变。
2. **双保真排序。** 用粗 FEM/流体近似筛候选，再用独立高保真求解器重排前几名。可省计算，风险是粗模型把真正好设计过早丢掉。
3. **小样本实物闭环。** 在同一制造工艺下打印基线和最优件，比较目标力学量而非仅比较仿真值。能检验模拟到实物的差距，风险是打印公差及材料差异。

### 6. [DeformSmith](https://arxiv.org/abs/2609.18620)：为生成流程加入主动探测并检验收益

1. **预算匹配消融。** 固定生成器与求解器，把 agent 选探测和预设探测在相同仿真次数下比较。可定位 agent 的增益，风险是提示词与候选空间不公平。
2. **失败热区驱动编辑。** 将应变集中/接触滑移映射到局部几何或材料块，只改热区；比较全局编辑。可提高可解释性，风险是最大应变处未必是根因。
3. **冻结后的新任务测试。** 校准完成后换负载位置和物体尺寸，测功能成功率与外观偏差。可检验资产复用性，风险是训练分布偏移过大。

### 7. [Cornell 多材料打印优化](https://arxiv.org/abs/2607.13174)：控制联合优化的搜索空间

1. **离散材料库。** 把连续组分限制为 2–3 种可打印材料，比较连续解和投影后解的目标损失。可提高可制造性，风险是投影使梯度失效。
2. **本构不确定性。** 对实验拟合的超弹性参数做扰动，优化最差或平均工况，并测未见加载曲线。可降低材料标定误差带来的失败，风险是过保守。
3. **几何/材料分步与联合对照。** 统一优化步数，比较只改拓扑、只改材料、两者联合。能确认联合编辑是否必要，风险是初始拓扑质量影响结论。

### 8. [DiffPhD](https://arxiv.org/abs/2605.14526)：让异质柔体梯度用于小预算编辑

1. **区域参数化。** 用少数区域模量代替逐单元场，在小四面体网格上比较梯度检查和未见载荷误差。可降低优化维度，风险是材料边界被平滑。
2. **接触梯度压力测试。** 在接触建立/消失附近比较伴随梯度与有限差分方向。可发现错误更新，风险是有限差分本身受离散噪声影响。
3. **逆物性与设计分阶段。** 先拟合探测响应、后锁定可辨识参数并改形状；与一步联合优化比较。可减少退化解，风险是错过有益耦合。

### 9. [Warp-Geo](https://arxiv.org/abs/2609.20964)：把可微几何接到柔体目标

1. **局部 SDF 基函数。** 仅更新目标受力区域附近的 SDF 系数，比较外观变化和力学目标。可保护资产身份，风险是目标需要全局传力路径改变。
2. **几何合法性。** 每步检查最小壁厚、连通性与体网格反转率；在小型夹爪案例比较有无约束的成功率。可防止仿真“作弊”，风险是约束增大优化难度。
3. **求解器外推。** 用另一网格尺度/时间步复核最终设计在未见边界条件下的响应。能区分稳健设计和离散化伪优，风险是计算量增加。

### 10. [PhysX-Omni](https://arxiv.org/abs/2605.21572)：检验“可仿真”是否等于“可用”

1. **功能探针套件。** 给每个生成柔体设置固定的压缩、拉伸、弯曲探针，报告力–位移曲线及网格有效率。可补强资产评价，风险是通用探针与任务脱节。
2. **少量实测更新。** 冻结生成模型，只用 1–3 次已知施力更新材料块，对照原始属性的未见力预测。可估计测试时校准收益，风险是生成内部结构错误。
3. **从可运行到可复用。** 固定一次校准资产，在第二种功能任务中测试，记录转换失败和接触异常。可衡量迁移，风险是仿真接口差异成为主要误差。

## 可复现的第一组实验

先用一种材料模型和三类目标验证问题是否成立，不需要训练大型生成器。可从已有单图 3D 资产中选取网格，冻结视觉表示，使用粗到细 FEM/MPM 与少量实体打印件。

| 功能族 | 允许编辑 | 已知探测 | 冻结后的未见评价 |
| --- | --- | --- | --- |
| 指定弯曲的柔性梁或夹爪 | 局部外形、2–3 区材料刚度 | 一个施力点的加载与卸载 | 新施力点/幅值下的力–位移曲线、目标端点位移 |
| 接触稳定的夹持垫 | 接触面几何、区域刚度，后续再加摩擦 | 已知法向压力与滑移起点 | 新物体曲率和载荷下的保持力、滑移率 |
| 缓冲或吸能件 | 传力几何、材料分布和密度 | 一个冲击速度/质量 | 未见冲击能量下的峰值传递力、回弹和永久形变 |

**必须同预算比较：**原始资产、仅几何编辑、仅材料编辑、联合编辑；固定探测、随机探测、agent 选探测；以及相同调用次数的无 agent 优化器。报告外观保持、体网格合法性、不可穿透、可制造性、计算时间和仿真调用次数。物性真值仅在可测时报告；真正的主指标是**校准之外**的功能响应与少量独立实物测量。

## 证据边界

- 目录中的“评价方式”说明论文**报告了什么类型的评价**，不表示本专题已经逐项复算结果。特别是 [DeformSmith](https://arxiv.org/abs/2609.18620) 的真实物理保真、[MeGAS](https://arxiv.org/abs/2606.23455) 的独立热物性测量，以及 [TourPhysics](https://arxiv.org/abs/2609.04911)、[PhysForge](https://arxiv.org/abs/2605.05163)、[P3Sim](https://arxiv.org/abs/2606.27575) 的数值指标需要回到正文逐项核对。
- 单图物性估计给出的是数据先验；只有已知外力、位移、接触或时间响应等额外观测，才有机会缩小隐藏参数的不确定性。即使如此，几何、模量、密度、阻尼和摩擦仍可能互相代偿。
- “可仿真”“与视频相似”“校准参数准确”“未见载荷功能成功”和“制造后实测有效”是不同证据层级。上面的具体研究问题与实验协议属于本专题提出的假设，不是已有论文的共同结论，也不声称全领域从未有人做过。
