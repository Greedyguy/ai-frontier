<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:47:53.507064",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "3D-Resampler",
    "VideoMME",
    "Reinforcement Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.82,
    "3D-Resampler": 0.71,
    "VideoMME": 0.69,
    "Reinforcement Learning": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Large Language Models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLMs"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is a trending area that bridges vision and language, making it highly connectable in the context of AI development.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "3D-Resampler model architecture",
        "canonical": "3D-Resampler",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel architecture specific to the paper, offering unique insights into efficient model design.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.81,
        "link_intent_score": 0.71
      },
      {
        "surface": "VideoMME benchmark",
        "canonical": "VideoMME",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The VideoMME benchmark is a specific evaluation metric that can link to performance comparisons in multimodal models.",
        "novelty_score": 0.68,
        "connectivity_score": 0.59,
        "specificity_score": 0.79,
        "link_intent_score": 0.69
      },
      {
        "surface": "hybrid reinforcement learning strategy",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "hybrid RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a foundational concept that supports the paper's methodology, linking to broader AI strategies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.83,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "efficiency",
      "performance",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Large Language Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "3D-Resampler model architecture",
      "resolved_canonical": "3D-Resampler",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.81,
        "link_intent": 0.71
      }
    },
    {
      "candidate_surface": "VideoMME benchmark",
      "resolved_canonical": "VideoMME",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.59,
        "specificity": 0.79,
        "link_intent": 0.69
      }
    },
    {
      "candidate_surface": "hybrid reinforcement learning strategy",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.83,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# MiniCPM-V 4.5: Cooking Efficient MLLMs via Architecture, Data, and Training Recipe

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18154.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18154](https://arxiv.org/abs/2509.18154)

## 🔗 유사한 논문
- [[2025-09-23/LEO-MINI_ An Efficient Multimodal Large Language Model using Conditional Token Reduction and Mixture of Multi-Modal Experts_20250923|LEO-MINI: An Efficient Multimodal Large Language Model using Conditional Token Reduction and Mixture of Multi-Modal Experts]] (85.5% similar)
- [[2025-09-24/Qianfan-VL_ Domain-Enhanced Universal Vision-Language Models_20250924|Qianfan-VL: Domain-Enhanced Universal Vision-Language Models]] (84.9% similar)
- [[2025-09-23/MCP_ A Control-Theoretic Orchestration Framework for Synergistic Efficiency and Interpretability in Multimodal Large Language Models_20250923|MCP: A Control-Theoretic Orchestration Framework for Synergistic Efficiency and Interpretability in Multimodal Large Language Models]] (84.6% similar)
- [[2025-09-23/When Big Models Train Small Ones_ Label-Free Model Parity Alignment for Efficient Visual Question Answering using Small VLMs_20250923|When Big Models Train Small Ones: Label-Free Model Parity Alignment for Efficient Visual Question Answering using Small VLMs]] (84.3% similar)
- [[2025-09-24/LCMF_ Lightweight Cross-Modality Mambaformer for Embodied Robotics VQA_20250924|LCMF: Lightweight Cross-Modality Mambaformer for Embodied Robotics VQA]] (84.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/3D-Resampler|3D-Resampler]], [[keywords/VideoMME|VideoMME]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18154v1 Announce Type: new 
Abstract: Multimodal Large Language Models (MLLMs) are undergoing rapid progress and represent the frontier of AI development. However, their training and inference efficiency have emerged as a core bottleneck in making MLLMs more accessible and scalable. To address the challenges, we present MiniCPM-V 4.5, an 8B parameter model designed for high efficiency and strong performance. We introduce three core improvements in model architecture, data strategy and training method: a unified 3D-Resampler model architecture for highly compact encoding over images and videos, a unified learning paradigm for document knowledge and text recognition without heavy data engineering, and a hybrid reinforcement learning strategy for proficiency in both short and long reasoning modes. Comprehensive experimental results in OpenCompass evaluation show that MiniCPM-V 4.5 surpasses widely used proprietary models such as GPT-4o-latest, and significantly larger open-source models such as Qwen2.5-VL 72B. Notably, the strong performance is achieved with remarkable efficiency. For example, on the widely adopted VideoMME benchmark, MiniCPM-V 4.5 achieves state-of-the-art performance among models under 30B size, using just 46.7\% GPU memory cost and 8.7\% inference time of Qwen2.5-VL 7B.

## 📝 요약

MiniCPM-V 4.5는 8억 개의 매개변수를 가진 모델로, 멀티모달 대형 언어 모델(MLLM)의 효율성과 성능을 개선하기 위해 개발되었습니다. 이 모델은 이미지와 비디오의 효율적인 인코딩을 위한 3D-Resampler 아키텍처, 문서 지식 및 텍스트 인식을 위한 통합 학습 패러다임, 그리고 짧고 긴 추론 모드 모두에 능숙한 하이브리드 강화 학습 전략을 도입했습니다. OpenCompass 평가에서 MiniCPM-V 4.5는 GPT-4o-latest와 같은 상용 모델 및 Qwen2.5-VL 72B와 같은 대규모 오픈소스 모델을 능가하는 성능을 보였습니다. 특히, VideoMME 벤치마크에서 30억 미만 크기의 모델 중 최첨단 성능을 달성하면서도 GPU 메모리 비용과 추론 시간을 크게 절감했습니다.

## 🎯 주요 포인트

- 1. MiniCPM-V 4.5는 8B 파라미터 모델로, 효율성과 성능을 동시에 높이기 위해 설계되었습니다.
- 2. 모델 아키텍처, 데이터 전략, 훈련 방법에서의 개선을 통해 이미지와 비디오의 인코딩을 위한 3D-Resampler 모델 아키텍처를 도입했습니다.
- 3. 문서 지식과 텍스트 인식을 위한 통합 학습 패러다임을 통해 복잡한 데이터 엔지니어링 없이 학습이 가능합니다.
- 4. 짧고 긴 추론 모드 모두에서 뛰어난 성능을 발휘하기 위해 하이브리드 강화 학습 전략을 채택했습니다.
- 5. MiniCPM-V 4.5는 VideoMME 벤치마크에서 30B 이하 모델 중 최첨단 성능을 기록하며, GPU 메모리 비용과 추론 시간을 크게 절감했습니다.


---

*Generated on 2025-09-24 14:47:53*