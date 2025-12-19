<p align="center" width="100%">
<a target="_blank"><img src="figs/FysicsWorld-logo.png" alt="" style="width: 50%; min-width: 200px; display: block; margin: auto;"></a>
</p>



<div align="center">
<br>
<h1>FysicsWorld: 统一的全模态理解、生成与推理评测基准</h1>

<h5 align="center"> 欢迎点击右上角的 [⭐ Star] 以便获取最新动态更新</h5>

<font size=7><div align='center' > 
[[🏠 主页](https://github.com/Fysics-AI/FysicsWorld)] 
[[📖 论文](https://arxiv.org/pdf/2512.12756)] 
[[🤗 数据集](https://huggingface.co/datasets/Fysics-AI/FysicsWorld)] 
[[👾 数据集 (魔搭)](https://www.modelscope.cn/datasets/Fysics-AI/FysicsWorld)] 
[[🏆 排行榜](https://huggingface.co/spaces/Fysics-AI/FysicsWorld-Leaderboard)]
  </div></font>

</div>

##  🚀  最新进展
- **`2025-12-14`** 我们正式推出了首个面向真实物理世界的统一全模态评测基准——[***FysicsWorld***](https://huggingface.co/datasets/Fysics-AI/FysicsWorld)。该基准不仅能够评测模型在图像、视频、音频与文本间进行双向输入与输出的能力，还覆盖对真实物理世界场景的感知、理解、生成以及跨模态推理等核心能力。



## 🎯 ***FysicsWorld*** 概述
<img src="figs/fig-teaser.jpg" width="100%" height="100%">

我们正式推出了 ***FysicsWorld***，这是首个支持图像、视频、音频与文本之间双向输入–输出的统一全模态基准，能够对真实物理世界的感知、理解、生成与推理等能力进行全面的 any-to-any 评测。该基准采用系统化的设计范式，任务覆盖从基础单模态感知到跨模态信息强耦合下的复杂推理过程，从而全面探索了当前多模态与全模态（omni-modal）架构的局限性与新兴优势。相较于现有的全模态与多模态基准，***FysicsWorld*** 具备以下优势：

 - **高质量 & 高度多样性：** ***FysicsWorld*** 以 8 个“多”维特性为核心特征，全面体现了其覆盖范围的广泛性、多样性与鲁棒性，具体包括：
    - 多维度（理解、生成、推理与语音交互）
    - 多模态（文本、图像、视频与音频的全模态I/O）
    - 多任务（16 项主要任务、200 余项子任务）
    - 多数据源（共 3,268 个样本，涵盖 40 余个数据源及人工筛选的网络数据）
    - 多领域（170 余个细粒度的开放领域类别）
    - 多类型（封闭式问答、开放式问答、多项选择题以及图像/视频/音频生成）
    - 多目标（评测对象涵盖全模态模型、通用多模态模型、特定模态的专用模型、以及统一理解生成模型）
    - 多重保障（多阶段质量控制策略）
- **跨模态融合依赖的推理：** 我们提出了一种全模态数据构建方法，称为 **“跨模态互补性筛选策略”** （Cross-Modal Complementarity Screening，CMCS）。该策略确保任务中保持跨模态强耦合关系，有效避免模型通过单一模态走捷径，从而强制实现真正的全模态融合的协同感知。
- **语音驱动的跨模态交互：** 为支持真实物理世界场景中跨模态交流与人机交互，我们构建了一套以语音为核心锚点的多模态数据生成流水线，在语音交互场景中同时保证语言流畅性与语义保真度，并涵盖 10 余种真实语音与语调。

基于 ***FysicsWorld***，我们对多种最先进模型进行了系统而全面的评测，包括全模态模型、通用多模态模型、特定模态的专用模型、以及统一理解生成模型，建立了统一的评测基线并揭示关键能力缺口，不仅为多模态模态架构的性能评估奠定了坚实基础，也为下一代新兴全模态架构实现真正的跨模态感知-理解-推理-生成指明了前进方向。


<p align="center">
    <img src="figs/fig-statiscs.jpg" width="100%" height="100%">
</p>

## 🔍 数据下载
完整数据集和相应的多媒体文件（图像、视频、音频）：

- 下载路径 1（🤗 HuggingFace）：[[链接](https://huggingface.co/datasets/Fysics-AI/FysicsWorld)]
- 下载路径 2（👾 ModelScope）：[[链接](https://www.modelscope.cn/datasets/Fysics-AI/FysicsWorld)]




## 🔮 基准评测

为确保评测协议的公平性与标准化，第一阶段我们公开发布完整的 ***FysicsWorld*** 数据集任务和问题，以及一个包含正确答案的 test-mini 子集（300 个样本），用于本地验证与调试。相应的问答数据分别位于 [./data](https://github.com/Fysics-AI/FysicsWorld/tree/main/data) 与 [./test-mini](https://github.com/Fysics-AI/FysicsWorld/tree/main/test-mini)中。

🕹️ **使用指南**:

1. 下载完整的 Fysics 数据集。
2. 按需选用 Fysics 中感兴趣的目标任务用于评测你的本地模型。
3. 遵循[评测指南](https://github.com/Fysics-AI/FysicsWorld/blob/main/eval/submission/EVALUATION.md)，将模型输出内容格式化为：[参考格式](https://github.com/Fysics-AI/FysicsWorld/blob/main/eval/submission/submission_format.json).
4. 将待测评结果发送至 *dicken@fyscis.ai*，我们会尽快给您反馈并在排行榜上更新您的成绩。



## 📈 评测结果
- **全模态/视觉语言大模型在图像为中心任务上的性能对比**

<p align="center">
    <img src="figs/tab-image.png" width="90%" height="100%">
</p>

*任务 ID:*
Task1-1 (图像理解), Task2-1 (语音驱动的图像理解), Task2-2 (图像-音频跨模态推理), Task2-3 (基于语音的图像内容问答), Task2-4 (基于图像人物角色的语音生成), and Task2-5 (基于图像内容的音频匹配)。

- **全模态/视觉语言大模型在视频为中心任务上的性能对比**

<p align="center">
    <img src="figs/tab-video.png" width="90%" height="100%">
</p>

*任务 ID:*
Task1-2 (视频理解), Task3-1 (语音驱动的视频理解), Task3-2 (视频-音频跨模态推理), Task3-3 (基于语音的图像内容问答), Task3-4 (基于图像人物角色的语音生成), Task3-5 (基于图像内容的音频匹配), and Task3-6 (基于视频动作序列和当前状态的后续行为预测)。

- **开源多模态大模型在部分模态支持的任务上的性能对比**

<p align="center">
    <img src="figs/fig-open-mllm.jpg" width="60%" height="100%">
</p>

*任务 ID:*
Task1-1 (图像理解), Task1-2 (视频理解), and Task3-6 (基于视频动作序列和当前状态的后续行为预测)。


- **不同模型在 (a)音频推理和 (b)视频生成任务上的性能对比**

<p align="center">
    <img src="figs/fig-exp-audio-video.jpg" width="90%" height="100%">
</p>


## 📖 引用

如果 ***FysicsWorld*** 对你的研究有所帮助，欢迎引用我们的工作。感谢支持！

```bibtex
@article{jiang2025fysicsworld,
    title={FysicsWorld: A Unified Full-Modality Benchmark for Any-to-Any Understanding, Generation, and Reasoning},
    author={Jiang, Yue and Yang, Dingkang and Han, Minghao and Han, Jinghang and Chen, Zizhi and Liu, Yizhou and Li, Mingcheng and Zhai, Peng and Zhang, Lihua},
    journal={arXiv preprint arXiv:2512.12756},
    year={2025}
}
```
