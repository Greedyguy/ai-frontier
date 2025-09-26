<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:47:16.331069",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Audio Language Models",
    "Knowledge Distillation",
    "Reasoning Capabilities",
    "Modality Gap",
    "Layer-wise Distillation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Audio Language Models": 0.78,
    "Knowledge Distillation": 0.82,
    "Reasoning Capabilities": 0.75,
    "Modality Gap": 0.73,
    "Layer-wise Distillation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "audio language models",
        "canonical": "Audio Language Models",
        "aliases": [
          "audio models",
          "speech models"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specialized area of machine learning focusing on audio data, distinct from general language models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "knowledge distillation",
        "canonical": "Knowledge Distillation",
        "aliases": [
          "model distillation",
          "teacher-student learning"
        ],
        "category": "specific_connectable",
        "rationale": "A critical method for transferring knowledge between models, relevant to the framework discussed.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "reasoning capabilities",
        "canonical": "Reasoning Capabilities",
        "aliases": [
          "reasoning skills",
          "logical reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's goal of enhancing audio models with reasoning abilities.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "modality gap",
        "canonical": "Modality Gap",
        "aliases": [
          "modality difference",
          "cross-modal gap"
        ],
        "category": "unique_technical",
        "rationale": "Describes a key challenge in integrating audio and textual data, relevant to the paper's framework.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.73
      },
      {
        "surface": "layer-wise distillation",
        "canonical": "Layer-wise Distillation",
        "aliases": [
          "layer alignment",
          "layer mapping"
        ],
        "category": "unique_technical",
        "rationale": "A specific technique within the proposed framework that enhances transfer efficiency.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "audio language models",
      "resolved_canonical": "Audio Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "knowledge distillation",
      "resolved_canonical": "Knowledge Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "reasoning capabilities",
      "resolved_canonical": "Reasoning Capabilities",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "modality gap",
      "resolved_canonical": "Modality Gap",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.73
      }
    },
    {
      "candidate_surface": "layer-wise distillation",
      "resolved_canonical": "Layer-wise Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Teaching Audio Models to Reason: A Unified Framework for Source- and Layer-wise Distillation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18579.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18579](https://arxiv.org/abs/2509.18579)

## 🔗 유사한 논문
- [[2025-09-22/SightSound-R1_ Cross-Modal Reasoning Distillation from Vision to Audio Language Models_20250922|SightSound-R1: Cross-Modal Reasoning Distillation from Vision to Audio Language Models]] (88.1% similar)
- [[2025-09-23/Audio-Reasoner_ Improving Reasoning Capability in Large Audio Language Models_20250923|Audio-Reasoner: Improving Reasoning Capability in Large Audio Language Models]] (87.0% similar)
- [[2025-09-19/Cross-Modal Knowledge Distillation for Speech Large Language Models_20250919|Cross-Modal Knowledge Distillation for Speech Large Language Models]] (85.9% similar)
- [[2025-09-23/SoundMind_ RL-Incentivized Logic Reasoning for Audio-Language Models_20250923|SoundMind: RL-Incentivized Logic Reasoning for Audio-Language Models]] (84.9% similar)
- [[2025-09-18/Omni-CLST_ Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering_20250918|Omni-CLST: Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering]] (84.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Knowledge Distillation|Knowledge Distillation]]
**⚡ Unique Technical**: [[keywords/Audio Language Models|Audio Language Models]], [[keywords/Reasoning Capabilities|Reasoning Capabilities]], [[keywords/Modality Gap|Modality Gap]], [[keywords/Layer-wise Distillation|Layer-wise Distillation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18579v1 Announce Type: cross 
Abstract: While large audio language models excel at tasks like ASR and emotion recognition, they still struggle with complex reasoning due to the modality gap between audio and text as well as the lack of structured intermediate supervision. To address this, we propose a unified knowledge distillation framework to transfer reasoning capabilities from a high-capacity textual teacher model to a student audio models while preserving its acoustic competence. Our method introduces two key dimensions: source-wise distillation, which leverages both textual and acoustic teachers to provide complementary modality-specific supervision; and layer-wise distillation, which aligns teacher signals with appropriate student layers to improve transfer efficiency. This dual-dimensional strategy enables fine-grained control over the distillation process, effectively bridging the gap between symbolic reasoning and speech representations. Experimental results show significant improvements in audio reasoning performance, demonstrating the effectiveness of our framework as a reasoning transfer solution for audio modeling.

## 📝 요약

이 논문은 오디오 언어 모델이 복잡한 추론 작업에서 겪는 어려움을 해결하기 위해 제안된 통합 지식 증류 프레임워크를 소개합니다. 이 방법은 고성능 텍스트 교사 모델의 추론 능력을 오디오 학생 모델로 전이하면서 음향적 역량을 유지합니다. 주요 기여는 텍스트와 오디오 교사를 활용한 소스 기반 증류와 교사 신호를 학생 모델의 적절한 층에 맞추는 층 기반 증류로, 이를 통해 상징적 추론과 음성 표현 간의 간극을 효과적으로 좁힙니다. 실험 결과, 오디오 추론 성능의 유의미한 향상을 보여주며, 제안된 프레임워크의 효용성을 입증합니다.

## 🎯 주요 포인트

- 1. 대형 오디오 언어 모델은 ASR 및 감정 인식과 같은 작업에서 뛰어나지만, 오디오와 텍스트 간의 모달리티 차이로 인해 복잡한 추론에는 어려움을 겪고 있습니다.
- 2. 제안된 통합 지식 증류 프레임워크는 고용량 텍스트 교사 모델의 추론 기능을 학생 오디오 모델로 전이하여 오디오 모델의 음향 역량을 유지합니다.
- 3. 소스 기반 증류와 층 기반 증류라는 두 가지 주요 차원을 도입하여 모달리티별 감독을 제공하고 전이 효율성을 향상시킵니다.
- 4. 이 이중 차원 전략은 증류 과정을 세밀하게 제어하여 상징적 추론과 음성 표현 간의 격차를 효과적으로 해소합니다.
- 5. 실험 결과, 오디오 추론 성능에서 유의미한 개선을 보여주며, 제안된 프레임워크의 효과성을 입증합니다.


---

*Generated on 2025-09-24 15:47:16*