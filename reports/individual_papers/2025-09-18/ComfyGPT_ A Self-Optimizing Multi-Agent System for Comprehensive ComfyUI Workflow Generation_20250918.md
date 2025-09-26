---
keywords:
  - Reinforcement Learning
  - Multi-Agent System
  - Workflow Generation
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2503.17671
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:35:00.008280",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Multi-Agent System",
    "Workflow Generation"
  ],
  "rejected_keywords": [
    "Large-Scale Dataset"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.8,
    "Multi-Agent System": 0.75,
    "Workflow Generation": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# ComfyGPT: A Self-Optimizing Multi-Agent System for Comprehensive ComfyUI Workflow Generation

**Korean Title:** ComfyGPT: 포괄적인 ComfyUI 워크플로우 생성을 위한 자기 최적화 다중 에이전트 시스템

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Multi-Agent System|Multi-Agent System]], [[keywords/Workflow Generation|Workflow Generation]]

## 🔗 유사한 논문
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (80.9% similar)
- [[AgentCTG Harnessing Multi-Agent Collaboration for Fine-Grained Precise Control in Text Generation]] (80.9% similar)
- [[$Agent^2$ An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (80.8% similar)
- [[LLM Agents for Interactive Workflow Provenance Reference Architecture and Evaluation Methodology]] (79.5% similar)
- [[DuetUI A Bidirectional Context Loop for Human-Agent Co-Generation of Task-Oriented Interfaces]] (79.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.17671v2 Announce Type: replace-cross 
Abstract: ComfyUI is a popular workflow-based interface that allows users to customize image generation tasks through an intuitive node-based system. However, the complexity of managing node connections and diverse modules can be challenging for users. In this paper, we introduce ComfyGPT, a self-optimizing multi-agent system designed to generate ComfyUI workflows based on task descriptions automatically. The key innovations of ComfyGPT include: (1) consisting of four specialized agents to build a multi-agent workflow generation system: ReformatAgent, FlowAgent, RefineAgent, and ExecuteAgent; (2) focusing on generating precise node connections instead of entire workflows, improving generation accuracy; and (3) enhancing workflow generation through reinforcement learning. Moreover, we introduce FlowDataset, a large-scale dataset containing 13,571 workflow-description pairs, and FlowBench, a comprehensive benchmark for evaluating workflow generation systems. Additionally, we propose four novel evaluation metrics: Format Validation (FV), Pass Accuracy (PA), Pass Instruct Alignment (PIA), and Pass Node Diversity (PND). Experimental results demonstrate that ComfyGPT significantly outperforms existing LLM-based methods in workflow generation, making it a significant step forward in this field. Code is avaliable at https://github.com/comfygpt/comfygpt.

## 🔍 Abstract (한글 번역)

arXiv:2503.17671v2 공지 유형: replace-cross
초록: ComfyUI는 사용자가 직관적인 노드 기반 시스템을 통해 이미지 생성 작업을 사용자 정의할 수 있도록 하는 인기 있는 워크플로 기반 인터페이스이다. 그러나 노드 연결과 다양한 모듈을 관리하는 복잡성은 사용자에게 어려움을 줄 수 있다. 본 논문에서는 작업 설명을 기반으로 ComfyUI 워크플로를 자동으로 생성하도록 설계된 자기 최적화 다중 에이전트 시스템인 ComfyGPT를 소개한다. ComfyGPT의 주요 혁신 사항은 다음과 같다: (1) 다중 에이전트 워크플로 생성 시스템을 구축하기 위한 네 개의 전문화된 에이전트로 구성: ReformatAgent, FlowAgent, RefineAgent, ExecuteAgent; (2) 전체 워크플로 대신 정확한 노드 연결 생성에 집중하여 생성 정확도를 향상시킴; (3) 강화학습을 통한 워크플로 생성 개선. 또한 13,571개의 워크플로-설명 쌍을 포함하는 대규모 데이터셋인 FlowDataset과 워크플로 생성 시스템을 평가하기 위한 포괄적인 벤치마크인 FlowBench를 소개한다. 추가적으로, 네 가지 새로운 평가 지표를 제안한다: Format Validation (FV), Pass Accuracy (PA), Pass Instruct Alignment (PIA), Pass Node Diversity (PND). 실험 결과는 ComfyGPT가 워크플로 생성에서 기존 LLM 기반 방법들을 상당히 능가하여 이 분야에서 중요한 진전을 이루었음을 보여준다. 코드는 https://github.com/comfygpt/comfygpt 에서 확인할 수 있다.

## 📝 요약

ComfyUI는 사용자들이 이미지 생성 작업을 직관적인 노드 기반 시스템으로 맞춤화할 수 있는 인기 있는 인터페이스입니다. 그러나 노드 연결과 다양한 모듈 관리의 복잡성은 사용자들에게 도전 과제가 될 수 있습니다. 본 논문에서는 ComfyGPT라는 자동화된 워크플로우 생성 시스템을 소개합니다. ComfyGPT는 ReformatAgent, FlowAgent, RefineAgent, ExecuteAgent로 구성된 네 개의 전문 에이전트를 통해 워크플로우를 생성하며, 전체 워크플로우 대신 정확한 노드 연결 생성에 중점을 두어 정확성을 높입니다. 강화 학습을 통해 워크플로우 생성을 개선하며, 13,571개의 워크플로우-설명 쌍을 포함한 대규모 데이터셋 FlowDataset과 평가 벤치마크 FlowBench를 도입합니다. 또한, 네 가지 평가 지표를 제안합니다. 실험 결과, ComfyGPT는 기존 방법들보다 우수한 성능을 보이며, 코드가 공개되어 있습니다.

## 🎯 주요 포인트

- 1. ComfyGPT는 작업 설명에 기반하여 ComfyUI 워크플로우를 자동으로 생성하는 자기 최적화 멀티 에이전트 시스템입니다.

- 2. ComfyGPT는 ReformatAgent, FlowAgent, RefineAgent, ExecuteAgent의 네 가지 전문 에이전트로 구성되어 있습니다.

- 3. ComfyGPT는 전체 워크플로우 대신 정확한 노드 연결 생성에 중점을 두어 생성 정확도를 향상시킵니다.

- 4. FlowDataset과 FlowBench를 소개하여 워크플로우 생성 시스템의 평가를 위한 대규모 데이터셋과 벤치마크를 제공합니다.

- 5. ComfyGPT는 기존 LLM 기반 방법들보다 워크플로우 생성에서 뛰어난 성능을 보입니다.

---

*Generated on 2025-09-19 11:03:06*