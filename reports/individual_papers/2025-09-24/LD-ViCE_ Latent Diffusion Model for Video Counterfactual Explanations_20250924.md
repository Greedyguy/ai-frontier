<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:36:41.798680",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Latent Diffusion Model",
    "Video Counterfactual Explanations",
    "Deep Learning",
    "Temporal Coherence"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Latent Diffusion Model": 0.78,
    "Video Counterfactual Explanations": 0.8,
    "Deep Learning": 0.75,
    "Temporal Coherence": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Latent Diffusion Model",
        "canonical": "Latent Diffusion Model",
        "aliases": [
          "LD-ViCE"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel framework for generating video counterfactual explanations, enhancing understanding of AI model behavior.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Video Counterfactual Explanations",
        "canonical": "Video Counterfactual Explanations",
        "aliases": [
          "Video Counterfactuals"
        ],
        "category": "unique_technical",
        "rationale": "Focuses on generating explanations for video-based AI systems, which is crucial for interpretability in safety-critical domains.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Central to the development and functioning of video-based AI systems, providing a foundation for understanding model behavior.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "Temporal Coherence",
        "canonical": "Temporal Coherence",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Key for ensuring explanations maintain consistency over time, critical for video analysis.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
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
      "candidate_surface": "Latent Diffusion Model",
      "resolved_canonical": "Latent Diffusion Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Video Counterfactual Explanations",
      "resolved_canonical": "Video Counterfactual Explanations",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Temporal Coherence",
      "resolved_canonical": "Temporal Coherence",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# LD-ViCE: Latent Diffusion Model for Video Counterfactual Explanations

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.08422.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.08422](https://arxiv.org/abs/2509.08422)

## 🔗 유사한 논문
- [[2025-09-23/VideoRFT_ Incentivizing Video Reasoning Capability in MLLMs via Reinforced Fine-Tuning_20250923|VideoRFT: Incentivizing Video Reasoning Capability in MLLMs via Reinforced Fine-Tuning]] (83.0% similar)
- [[2025-09-23/VidCLearn_ A Continual Learning Approach for Text-to-Video Generation_20250923|VidCLearn: A Continual Learning Approach for Text-to-Video Generation]] (82.7% similar)
- [[2025-09-23/V-CECE_ Visual Counterfactual Explanations via Conceptual Edits_20250923|V-CECE: Visual Counterfactual Explanations via Conceptual Edits]] (82.6% similar)
- [[2025-09-23/Automated Procedural Analysis via Video-Language Models for AI-assisted Nursing Skills Assessment_20250923|Automated Procedural Analysis via Video-Language Models for AI-assisted Nursing Skills Assessment]] (82.3% similar)
- [[2025-09-24/Injecting Explainability and Lightweight Design into Weakly Supervised Video Anomaly Detection Systems_20250924|Injecting Explainability and Lightweight Design into Weakly Supervised Video Anomaly Detection Systems]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Temporal Coherence|Temporal Coherence]]
**⚡ Unique Technical**: [[keywords/Latent Diffusion Model|Latent Diffusion Model]], [[keywords/Video Counterfactual Explanations|Video Counterfactual Explanations]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.08422v2 Announce Type: replace-cross 
Abstract: Video-based AI systems are increasingly adopted in safety-critical domains such as autonomous driving and healthcare. However, interpreting their decisions remains challenging due to the inherent spatiotemporal complexity of video data and the opacity of deep learning models. Existing explanation techniques often suffer from limited temporal coherence, insufficient robustness, and a lack of actionable causal insights. Current counterfactual explanation methods typically do not incorporate guidance from the target model, reducing semantic fidelity and practical utility. We introduce Latent Diffusion for Video Counterfactual Explanations (LD-ViCE), a novel framework designed to explain the behavior of video-based AI models. Compared to previous approaches, LD-ViCE reduces the computational costs of generating explanations by operating in latent space using a state-of-the-art diffusion model, while producing realistic and interpretable counterfactuals through an additional refinement step. Our experiments demonstrate the effectiveness of LD-ViCE across three diverse video datasets, including EchoNet-Dynamic (cardiac ultrasound), FERV39k (facial expression), and Something-Something V2 (action recognition). LD-ViCE outperforms a recent state-of-the-art method, achieving an increase in R2 score of up to 68% while reducing inference time by half. Qualitative analysis confirms that LD-ViCE generates semantically meaningful and temporally coherent explanations, offering valuable insights into the target model behavior. LD-ViCE represents a valuable step toward the trustworthy deployment of AI in safety-critical domains.

## 📝 요약

LD-ViCE는 비디오 기반 AI 모델의 행동을 설명하기 위한 새로운 프레임워크로, 안전이 중요한 분야에서 AI의 신뢰성을 높입니다. 이 방법은 최첨단 확산 모델을 활용하여 잠재 공간에서 작동함으로써 설명 생성의 계산 비용을 줄이고, 추가적인 정제 과정을 통해 현실적이고 해석 가능한 반사실적 설명을 제공합니다. EchoNet-Dynamic, FERV39k, Something-Something V2 등 다양한 비디오 데이터셋에서 LD-ViCE는 기존 방법보다 최대 68% 높은 R2 점수를 기록하며, 추론 시간을 절반으로 단축했습니다. 질적 분석 결과, LD-ViCE는 의미론적으로 유의미하고 시간적으로 일관된 설명을 생성하여 모델의 행동에 대한 귀중한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. LD-ViCE는 비디오 기반 AI 모델의 행동을 설명하기 위한 새로운 프레임워크로, 잠재 공간에서 작동하여 설명 생성의 계산 비용을 줄입니다.
- 2. LD-ViCE는 최신 확산 모델을 사용하여 현실적이고 해석 가능한 반사실적 설명을 생성하며, 추가적인 정제 단계를 통해 이를 개선합니다.
- 3. 실험 결과, LD-ViCE는 EchoNet-Dynamic, FERV39k, Something-Something V2 등 세 가지 다양한 비디오 데이터셋에서 효과적임을 입증했습니다.
- 4. LD-ViCE는 최신 방법보다 최대 68% 높은 R2 점수를 기록하며 추론 시간을 절반으로 줄였습니다.
- 5. LD-ViCE는 의미적으로 유의미하고 시간적으로 일관된 설명을 생성하여 안전이 중요한 분야에서 AI의 신뢰할 수 있는 배포를 위한 중요한 진전을 제공합니다.


---

*Generated on 2025-09-24 15:36:41*