# Gentopia 
*The Collective Growth of Intelligent Agents.* 🦙🌎

Gentopia is a lightweight and extensible framework for LLM-driven Agents and [ALM](https://arxiv.org/abs/2302.07842)  research. It provides multiple essential components to build, test and evaluate agents. At its core, Gentopia aims to embody agents with single config files, thus minimizing your effort in maintaining, tuning, and sharing agents.

Gentopia maintains an agent zoo [GentPool](https://github.com/Gentopia-AI/GentPool) to share public agents specialized for different tasks. In this platform, you could easily *interact* with other agents by cloning, hierarchical plug-in, or sharing environment. We also build a unique agent [benchmark](https://gentopia.readthedocs.io/en/latest/gentpool.html#agent-evaluation) for holistic ALM evaluation. 

## Motivation 🧠
Agent practitioners start to realize the difficulty in tuning a "well-rounded" agent with tons of tools or instructions in single layer.
Recent studies like [TinyStories](https://arxiv.org/abs/2301.12726), [Specializing Reasoning](https://arxiv.org/abs/2301.12726), [Let's Verify SbS](https://arxiv.org/abs/2305.20050), [ReWOO](https://arxiv.org/abs/2305.18323), etc. also point us towards an intuitive yet undervalued direction 👉 

```
An LLM is more capable if you create a context/distribution shift specialized to some target tasks.
```
Sadly, there is no silver bullet for agent specialization. For example, you can 
- Simply add `Let's think step by step.` in your **prompt** for more accurate Math QA.
- Give a **few-shot** exemplar in your prompt to guide a better reasoning trajectory for novel plotting.
- Supervise **fine-tuning** (SFT) your 70B `llama2` like [this](https://arxiv.org/abs/2305.20050) to match reasoning of 175B GPT-3.5.
- Tune your agent **paradigm** like this [demo](https://www.youtube.com/watch?v=diJ4IDaT4Z4) to easily half the execution time for Seach & Summarize.
- And more ...

Isn't it beautiful if one shares his specialized intelligence, allowing others to reproduce, build on, or interact with it at ease? 🤗 This belief inspires us to build Gentopia, 
**designed for agent *specialization, sharing, and interaction,* to achieve collective growth towards greater intelligence**.

## Core Features 💡

- ⚙️ Config-driven agent assembling and chat.
- 🚀 Large amount of prebuilt agent types, LLM clients, tools, memory systems, and more.
- 🪶 Lightweight and highly extensible implementation of essential components.
- 🧪 Aligning with state-of-the-art AI research.
- 🤝 Enabling multi-agent interactions.
- 🦁 Unique platform of agent zoo and eval benchmark.

## Quick Start 🛫
```
pip install gentopia
```
or if you want to build with open LLMs locally 👉 `pip install gentopia[huggingface]`

First time to Gentopia? Grab a coffee ☕ and take ~ 10 mins to check out the following mind-blowing demos 👀 🤯

<div style="display: flex; justify-content: space-around;">
  
<a href="https://www.youtube.com/watch?v=7dZ3ZvsI7sw" target="_blank">
  <img src="https://img.youtube.com/vi/7dZ3ZvsI7sw/hqdefault.jpg" alt="Video 1" style="width:32%;">
</a>

<a href="https://www.youtube.com/watch?v=XTsv9pk6AOA" target="_blank">
  <img src="https://img.youtube.com/vi/XTsv9pk6AOA/hqdefault.jpg" alt="Video 2" style="width:32%;">
</a>

<a href="https://www.youtube.com/watch?v=diJ4IDaT4Z4" target="_blank">
  <img src="https://img.youtube.com/vi/diJ4IDaT4Z4/hqdefault.jpg" alt="Video 3" style="width:32%;">
</a>

</div>

(Jump to the third one if you only have 3 mins 🤫)

## Documentation 📖
See [here](https://gentopia.readthedocs.io/en/latest/index.html) for full documentation.

🌟 Highlight Topics 
- [Agent Templates](https://gentopia.readthedocs.io/en/latest/quick_start.html#vanilla-agent)
- [Hierarchical Agents](https://gentopia.readthedocs.io/en/latest/agent_components.html#agent-as-plugin)
- [Unique Agent Benchmark](https://gentopia.readthedocs.io/en/latest/gentpool.html#agent-evaluation)
- [Open LLM Supports](https://gentopia.readthedocs.io/en/latest/agent_components.html#huggingface-open-llms)
- [High-Performance Memory](https://gentopia.readthedocs.io/en/latest/agent_components.html#long-short-term-memory)

## Build with us 🌎

Participate in this Utopia of superintelligence and help it grows! As a fully open-source project, we develop under public advice, ideas, and supervision. Meanwhile, here are ways you may contribute to Gentopia.

- 🐛 Post an [issue](https://github.com/Gentopia-AI/Gentopia/issues) requesting necessary bug fixes, additional features, or roadmap suggestions. (Check closed ones first)
- 🎯 Our dev team meets weekly to groom [backlog](https://github.com/orgs/Gentopia-AI/projects/1) into tickets. While we work on them, you can pick up others and create a [Pull Request](https://github.com/Gentopia-AI/Gentopia/pulls) to request a merge. We always welcome new members in this way.
- 🤝 Share your specialized agent to [GentPool](https://github.com/Gentopia-AI/GentPool)! Create an Agent PR ([example]()) to merge your well-tuned agent into the pool. This allows others to use or build upon your agent. 
- ⭐ Help us spread! Give us a star, follow us on [Twitter](https://twitter.com/GentopiaAI), join our [Discord](https://discord.gg/ASPP9MY9QK), and share with your friends!  


