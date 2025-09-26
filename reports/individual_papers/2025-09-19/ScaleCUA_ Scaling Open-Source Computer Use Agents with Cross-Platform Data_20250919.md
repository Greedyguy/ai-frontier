---
keywords:
  - Vision-Language Models
  - Computer Use Agents
  - Cross-Platform Data
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15221
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:25:13.039852",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Models",
    "Computer Use Agents",
    "Cross-Platform Data"
  ],
  "rejected_keywords": [
    "Foundation Models"
  ],
  "similarity_scores": {
    "Vision-Language Models": 0.88,
    "Computer Use Agents": 0.8,
    "Cross-Platform Data": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data

**Korean Title:** ScaleCUA: 플랫폼 간 데이터로 오픈 소스 컴퓨터 사용 에이전트 확장

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Computer Use Agents|Computer Use Agents]], [[keywords/Cross-Platform Data|Cross-Platform Data]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Models|Vision-Language Models]]

## 🔗 유사한 논문
- [[UnifiedVisual A Framework for Constructing Unified Vision-Language Datasets]] (83.5% similar)
- [[VeriOS Query-Driven Proactive Human-Agent-GUI Interaction for Trustworthy OS Agents]] (80.8% similar)
- [[AppAgent v2 Advanced Agent for Flexible Mobile Interactions]] (80.3% similar)
- [[SAIL-VL2 Technical Report_20250918|SAIL-VL2 Technical Report]] (80.1% similar)
- [[Apertus Democratizing Open and Compliant LLMs for Global Language Environments]] (79.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15221v1 Announce Type: new 
Abstract: Vision-Language Models (VLMs) have enabled computer use agents (CUAs) that operate GUIs autonomously, showing great potential, yet progress is limited by the lack of large-scale, open-source computer use data and foundation models. In this work, we introduce ScaleCUA, a step toward scaling open-source CUAs. It offers a large-scale dataset spanning 6 operating systems and 3 task domains, built via a closed-loop pipeline uniting automated agents with human experts. Trained on this scaled-up data, ScaleCUA can operate seamlessly across platforms. Specifically, it delivers strong gains over baselines (+26.6 on WebArena-Lite-v2, +10.7 on ScreenSpot-Pro) and sets new state-of-the-art results (94.4% on MMBench-GUI L1-Hard, 60.6% on OSWorld-G, 47.4% on WebArena-Lite-v2). These findings underscore the power of data-driven scaling for general-purpose computer use agents. We will release data, models, and code to advance future research: https://github.com/OpenGVLab/ScaleCUA.

## 🔍 Abstract (한글 번역)

arXiv:2509.15221v1 발표 유형: 신규  
초록: 비전-언어 모델(VLMs)은 GUI를 자율적으로 작동하는 컴퓨터 사용 에이전트(CUAs)를 가능하게 하여 큰 잠재력을 보여주고 있지만, 대규모 오픈 소스 컴퓨터 사용 데이터와 기초 모델의 부족으로 인해 발전이 제한되고 있습니다. 본 연구에서는 오픈 소스 CUA의 확장을 위한 단계로서 ScaleCUA를 소개합니다. 이는 자동화된 에이전트와 인간 전문가를 결합한 폐쇄 루프 파이프라인을 통해 구축된, 6개의 운영 체제와 3개의 작업 도메인을 아우르는 대규모 데이터셋을 제공합니다. 이 확장된 데이터로 훈련된 ScaleCUA는 플랫폼 간에 원활하게 작동할 수 있습니다. 특히, 이는 기준선 대비 강력한 향상을 제공하며(+26.6 WebArena-Lite-v2에서, +10.7 ScreenSpot-Pro에서), 새로운 최첨단 결과를 설정합니다(MMBench-GUI L1-Hard에서 94.4%, OSWorld-G에서 60.6%, WebArena-Lite-v2에서 47.4%). 이러한 결과는 범용 컴퓨터 사용 에이전트를 위한 데이터 기반 확장의 힘을 강조합니다. 우리는 향후 연구를 발전시키기 위해 데이터, 모델 및 코드를 공개할 것입니다: https://github.com/OpenGVLab/ScaleCUA.

## 📝 요약

Vision-Language Models(VLMs)를 활용한 컴퓨터 사용 에이전트(CUAs)의 발전은 대규모 오픈소스 데이터의 부족으로 제한되었습니다. 본 연구에서는 이를 해결하기 위해 ScaleCUA를 소개합니다. 이는 6개의 운영 체제와 3개의 작업 도메인을 아우르는 대규모 데이터셋을 제공하며, 자동화된 에이전트와 인간 전문가를 결합한 폐쇄 루프 파이프라인을 통해 구축되었습니다. ScaleCUA는 다양한 플랫폼에서 원활하게 작동하며, 기존 기준을 크게 초과하는 성능을 보여줍니다(WebArena-Lite-v2에서 +26.6, ScreenSpot-Pro에서 +10.7). 또한 MMBench-GUI L1-Hard에서 94.4%, OSWorld-G에서 60.6%, WebArena-Lite-v2에서 47.4%로 새로운 최고 성능을 기록했습니다. 이러한 결과는 데이터 기반 확장의 중요성을 강조하며, 향후 연구를 위해 데이터, 모델, 코드를 공개할 예정입니다.

## 🎯 주요 포인트

- 1. Vision-Language Models(VLMs)는 GUI를 자율적으로 작동하는 컴퓨터 사용 에이전트(CUAs)를 가능하게 하지만, 대규모 오픈소스 데이터와 기초 모델의 부족으로 발전이 제한되고 있습니다.

- 2. ScaleCUA는 6개의 운영 체제와 3개의 작업 도메인을 아우르는 대규모 데이터셋을 제공하여 오픈소스 CUAs의 확장을 목표로 합니다.

- 3. ScaleCUA는 다양한 플랫폼에서 원활하게 작동하며, 기존 기준을 크게 초과하는 성능을 보여주고 새로운 최첨단 결과를 설정했습니다.

- 4. 데이터 기반 확장이 범용 컴퓨터 사용 에이전트의 강력한 가능성을 강조하며, 향후 연구를 위해 데이터, 모델, 코드를 공개할 예정입니다.

---

*Generated on 2025-09-19 16:11:02*