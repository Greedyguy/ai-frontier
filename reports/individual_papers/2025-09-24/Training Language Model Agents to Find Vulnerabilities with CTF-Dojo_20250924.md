<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:35:29.096982",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "CTF-Dojo",
    "Execution-grounded Training",
    "Capture-The-Flag Challenges"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "CTF-Dojo": 0.8,
    "Execution-grounded Training": 0.78,
    "Capture-The-Flag Challenges": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's methodology and connect well with existing literature on language models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "CTF-Dojo",
        "canonical": "CTF-Dojo",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "CTF-Dojo is a novel framework introduced in the paper, essential for understanding the specific contributions of the research.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Execution-grounded training",
        "canonical": "Execution-grounded Training",
        "aliases": [
          "Execution-based Training"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is pivotal for linking the paper's approach to broader trends in training methodologies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Capture-The-Flag challenges",
        "canonical": "Capture-The-Flag Challenges",
        "aliases": [
          "CTF Challenges"
        ],
        "category": "unique_technical",
        "rationale": "Capture-The-Flag challenges are central to the experimental setup and are a unique aspect of the paper's contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "CTF-Dojo",
      "resolved_canonical": "CTF-Dojo",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Execution-grounded training",
      "resolved_canonical": "Execution-grounded Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Capture-The-Flag challenges",
      "resolved_canonical": "Capture-The-Flag Challenges",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Training Language Model Agents to Find Vulnerabilities with CTF-Dojo

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2508.18370.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2508.18370](https://arxiv.org/abs/2508.18370)

## 🔗 유사한 논문
- [[2025-09-23/Generalizable End-to-End Tool-Use RL with Synthetic CodeGym_20250923|Generalizable End-to-End Tool-Use RL with Synthetic CodeGym]] (86.6% similar)
- [[2025-09-19/From Capabilities to Performance_ Evaluating Key Functional Properties of LLM Architectures in Penetration Testing_20250919|From Capabilities to Performance: Evaluating Key Functional Properties of LLM Architectures in Penetration Testing]] (86.5% similar)
- [[2025-09-22/Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges_20250922|Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges]] (85.8% similar)
- [[2025-09-23/Large Language Models for Cyber Security_ A Systematic Literature Review_20250923|Large Language Models for Cyber Security: A Systematic Literature Review]] (84.4% similar)
- [[2025-09-23/Sugar-Coated Poison_ Benign Generation Unlocks LLM Jailbreaking_20250923|Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking]] (84.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Execution-grounded Training|Execution-grounded Training]]
**⚡ Unique Technical**: [[keywords/CTF-Dojo|CTF-Dojo]], [[keywords/Capture-The-Flag Challenges|Capture-The-Flag Challenges]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.18370v2 Announce Type: replace-cross 
Abstract: Large language models (LLMs) have demonstrated exceptional capabilities when trained within executable runtime environments, notably excelling at software engineering tasks through verified feedback loops. Yet, scalable and generalizable execution-grounded environments remain scarce, limiting progress in training more capable ML agents. We introduce CTF-Dojo, the first large-scale executable runtime tailored for training LLMs with verifiable feedback, featuring 658 fully functional Capture-The-Flag (CTF)-style challenges containerized in Docker with guaranteed reproducibility. To enable rapid scaling without manual intervention, we develop CTF-Forge, an automated pipeline that transforms publicly available artifacts into ready-to-use execution environments in minutes, eliminating weeks of expert configuration traditionally required. We trained LLM-based agents on just 486 high-quality, execution-verified trajectories from CTF-Dojo, achieving up to 11.6% absolute gains over strong baselines across three competitive benchmarks: InterCode-CTF, NYU CTF Bench, and Cybench. Our best-performing 32B model reaches 31.9% Pass@1, establishing a new open-weight state-of-the-art that rivals frontier models like DeepSeek-V3-0324 and Gemini-2.5-Flash. By framing CTF-style tasks as a benchmark for executable-agent learning, CTF-Dojo demonstrates that execution-grounded training signals are not only effective but pivotal in advancing high-performance ML agents without dependence on costly proprietary systems.

## 📝 요약

이 논문은 실행 가능한 런타임 환경에서 대규모 언어 모델(LLM)의 훈련을 위한 CTF-Dojo를 소개합니다. CTF-Dojo는 658개의 CTF 스타일 도전을 Docker로 컨테이너화하여 검증 가능한 피드백을 제공합니다. 또한, CTF-Forge라는 자동화 파이프라인을 개발하여 공공 자료를 신속하게 실행 환경으로 변환합니다. 이를 통해 LLM 기반 에이전트를 훈련하여 InterCode-CTF, NYU CTF Bench, Cybench에서 최대 11.6%의 성능 향상을 달성했습니다. 특히, 32B 모델은 Pass@1에서 31.9%를 기록하며 최고 성능을 보였습니다. CTF-Dojo는 실행 기반 훈련이 고성능 ML 에이전트 개발에 효과적임을 증명합니다.

## 🎯 주요 포인트

- 1. CTF-Dojo는 대규모 실행 가능한 런타임 환경으로, 658개의 CTF 스타일 챌린지를 통해 LLMs의 검증 가능한 피드백 기반 훈련을 지원합니다.
- 2. CTF-Forge는 공개된 아티팩트를 신속하게 실행 환경으로 전환하는 자동화 파이프라인으로, 전문가의 수주간의 설정 작업을 불필요하게 만듭니다.
- 3. CTF-Dojo에서 훈련된 LLM 기반 에이전트는 InterCode-CTF, NYU CTF Bench, Cybench에서 최대 11.6%의 성능 향상을 보였습니다.
- 4. 32B 모델은 31.9%의 Pass@1을 기록하며, DeepSeek-V3-0324 및 Gemini-2.5-Flash와 같은 최첨단 모델에 필적하는 성능을 보여줍니다.
- 5. CTF-Dojo는 실행 기반 훈련 신호가 고성능 ML 에이전트 발전에 효과적이며, 비용이 많이 드는 독점 시스템에 의존하지 않고도 가능함을 입증합니다.


---

*Generated on 2025-09-24 15:35:29*