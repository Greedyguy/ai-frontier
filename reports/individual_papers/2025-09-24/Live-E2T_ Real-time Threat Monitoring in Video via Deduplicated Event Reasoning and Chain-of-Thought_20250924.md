<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:02:43.814510",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Chain-of-Thought Reasoning",
    "Semantic Tuples",
    "Event Deduplication"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Chain-of-Thought Reasoning": 0.78,
    "Semantic Tuples": 0.72,
    "Event Deduplication": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "The use of Large Language Models is central to the framework's reasoning capability, linking it to broader NLP advancements.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Chain-of-Thought strategy",
        "canonical": "Chain-of-Thought Reasoning",
        "aliases": [
          "CoT"
        ],
        "category": "unique_technical",
        "rationale": "This strategy is a unique approach for enhancing logical reasoning in threat assessment, linking to cognitive reasoning models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Human-Object-Interaction-Place semantic tuples",
        "canonical": "Semantic Tuples",
        "aliases": [
          "HOIP tuples"
        ],
        "category": "unique_technical",
        "rationale": "This novel representation method enhances the semantic understanding of video data, linking to structured data representation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Event Deduplication",
        "canonical": "Event Deduplication",
        "aliases": [
          "Redundancy Filtering"
        ],
        "category": "specific_connectable",
        "rationale": "This mechanism ensures real-time performance by reducing data redundancy, linking to data processing techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "real-time",
      "framework",
      "methodologies",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Chain-of-Thought strategy",
      "resolved_canonical": "Chain-of-Thought Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Human-Object-Interaction-Place semantic tuples",
      "resolved_canonical": "Semantic Tuples",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Event Deduplication",
      "resolved_canonical": "Event Deduplication",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Live-E2T: Real-time Threat Monitoring in Video via Deduplicated Event Reasoning and Chain-of-Thought

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18571.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18571](https://arxiv.org/abs/2509.18571)

## 🔗 유사한 논문
- [[2025-09-24/LD-ViCE_ Latent Diffusion Model for Video Counterfactual Explanations_20250924|LD-ViCE: Latent Diffusion Model for Video Counterfactual Explanations]] (83.8% similar)
- [[2025-09-23/AHA -- Predicting What Matters Next_ Online Highlight Detection Without Looking Ahead_20250923|AHA -- Predicting What Matters Next: Online Highlight Detection Without Looking Ahead]] (83.4% similar)
- [[2025-09-23/VideoRFT_ Incentivizing Video Reasoning Capability in MLLMs via Reinforced Fine-Tuning_20250923|VideoRFT: Incentivizing Video Reasoning Capability in MLLMs via Reinforced Fine-Tuning]] (82.8% similar)
- [[2025-09-22/ChronoForge-RL_ Chronological Forging through Reinforcement Learning for Enhanced Video Understanding_20250922|ChronoForge-RL: Chronological Forging through Reinforcement Learning for Enhanced Video Understanding]] (81.3% similar)
- [[2025-09-23/Full-History Graphs with Edge-Type Decoupled Networks for Temporal Reasoning_20250923|Full-History Graphs with Edge-Type Decoupled Networks for Temporal Reasoning]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Event Deduplication|Event Deduplication]]
**⚡ Unique Technical**: [[keywords/Chain-of-Thought Reasoning|Chain-of-Thought Reasoning]], [[keywords/Semantic Tuples|Semantic Tuples]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18571v1 Announce Type: new 
Abstract: Real-time threat monitoring identifies threatening behaviors in video streams and provides reasoning and assessment of threat events through explanatory text. However, prevailing methodologies, whether based on supervised learning or generative models, struggle to concurrently satisfy the demanding requirements of real-time performance and decision explainability. To bridge this gap, we introduce Live-E2T, a novel framework that unifies these two objectives through three synergistic mechanisms. First, we deconstruct video frames into structured Human-Object-Interaction-Place semantic tuples. This approach creates a compact, semantically focused representation, circumventing the information degradation common in conventional feature compression. Second, an efficient online event deduplication and updating mechanism is proposed to filter spatio-temporal redundancies, ensuring the system's real time responsiveness. Finally, we fine-tune a Large Language Model using a Chain-of-Thought strategy, endow it with the capability for transparent and logical reasoning over event sequences to produce coherent threat assessment reports. Extensive experiments on benchmark datasets, including XD-Violence and UCF-Crime, demonstrate that Live-E2T significantly outperforms state-of-the-art methods in terms of threat detection accuracy, real-time efficiency, and the crucial dimension of explainability.

## 📝 요약

논문은 실시간 위협 모니터링을 위한 새로운 프레임워크인 Live-E2T를 소개합니다. 이 프레임워크는 실시간 성능과 설명 가능성을 동시에 만족시키기 위해 세 가지 메커니즘을 통합합니다. 첫째, 비디오 프레임을 사람-객체-장소의 의미론적 튜플로 분해하여 정보 손실을 최소화합니다. 둘째, 효율적인 온라인 이벤트 중복 제거 및 업데이트 메커니즘을 통해 공간적, 시간적 중복성을 필터링하여 실시간 반응성을 보장합니다. 셋째, 대형 언어 모델을 체인 오브 쏘트 전략으로 미세 조정하여 이벤트 시퀀스에 대한 투명하고 논리적인 추론을 가능하게 합니다. 실험 결과, Live-E2T는 XD-Violence와 UCF-Crime 등의 데이터셋에서 위협 탐지 정확도, 실시간 효율성, 설명 가능성 측면에서 기존 방법들보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. Live-E2T는 실시간 성능과 설명 가능성을 동시에 만족시키기 위해 세 가지 상호 보완적인 메커니즘을 도입한 새로운 프레임워크입니다.
- 2. 비디오 프레임을 Human-Object-Interaction-Place 의미론적 튜플로 분해하여 정보 손실을 최소화하고, 의미 중심의 압축 표현을 만듭니다.
- 3. 효율적인 온라인 이벤트 중복 제거 및 업데이트 메커니즘을 통해 시공간 중복성을 필터링하여 시스템의 실시간 응답성을 보장합니다.
- 4. 대형 언어 모델을 Chain-of-Thought 전략으로 미세 조정하여 이벤트 시퀀스에 대한 투명하고 논리적인 추론을 통해 일관된 위협 평가 보고서를 생성합니다.
- 5. XD-Violence와 UCF-Crime 등 벤치마크 데이터셋에서의 실험 결과, Live-E2T는 위협 탐지 정확성, 실시간 효율성, 설명 가능성 측면에서 최첨단 방법들을 능가합니다.


---

*Generated on 2025-09-24 16:02:43*