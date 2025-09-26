<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:50:10.496921",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Attention Mechanism",
    "LAWCAT",
    "Convolutional Layers",
    "Mistral-7B",
    "Llama3.2-1B"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Attention Mechanism": 0.78,
    "LAWCAT": 0.8,
    "Convolutional Layers": 0.7,
    "Mistral-7B": 0.75,
    "Llama3.2-1B": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Linear Attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Linearized Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the broader concept of attention mechanisms, crucial for understanding the paper's contribution.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "LAWCAT",
        "canonical": "LAWCAT",
        "aliases": [
          "Linear Attention with Convolution Across Time"
        ],
        "category": "unique_technical",
        "rationale": "Represents the novel framework introduced in the paper, essential for understanding its unique contribution.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Conv1D layers",
        "canonical": "Convolutional Layers",
        "aliases": [
          "1D Convolutional Layers"
        ],
        "category": "broad_technical",
        "rationale": "Connects to the well-known concept of convolutional layers, relevant for understanding the model architecture.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "Mistral-7B",
        "canonical": "Mistral-7B",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Specific model variant used in the study, important for contextualizing results.",
        "novelty_score": 0.8,
        "connectivity_score": 0.5,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Llama3.2-1B",
        "canonical": "Llama3.2-1B",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Another specific model variant, highlighting the paper's experimental scope.",
        "novelty_score": 0.82,
        "connectivity_score": 0.52,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "long-context applications",
      "pre-training tokens"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Linear Attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "LAWCAT",
      "resolved_canonical": "LAWCAT",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Conv1D layers",
      "resolved_canonical": "Convolutional Layers",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Mistral-7B",
      "resolved_canonical": "Mistral-7B",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.5,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Llama3.2-1B",
      "resolved_canonical": "Llama3.2-1B",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.52,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# LAWCAT: Efficient Distillation from Quadratic to Linear Attention with Convolution across Tokens for Long Context Modeling

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18467.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18467](https://arxiv.org/abs/2509.18467)

## 🔗 유사한 논문
- [[2025-09-23/Language Modeling with Learned Meta-Tokens_20250923|Language Modeling with Learned Meta-Tokens]] (82.5% similar)
- [[2025-09-23/EG-MLA_ Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs_20250923|EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs]] (81.7% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (81.7% similar)
- [[2025-09-23/TACO_ Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration_20250923|TACO: Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration]] (81.6% similar)
- [[2025-09-23/Scaling Efficient LLMs_20250923|Scaling Efficient LLMs]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Convolutional Layers|Convolutional Layers]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/LAWCAT|LAWCAT]], [[keywords/Mistral-7B|Mistral-7B]], [[keywords/Llama3.2-1B|Llama3.2-1B]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18467v1 Announce Type: cross 
Abstract: Although transformer architectures have achieved state-of-the-art performance across diverse domains, their quadratic computational complexity with respect to sequence length remains a significant bottleneck, particularly for latency-sensitive long-context applications. While recent linear-complexity alternatives are increasingly powerful, effectively training them from scratch is still resource-intensive. To overcome these limitations, we propose LAWCAT (Linear Attention with Convolution Across Time), a novel linearization framework designed to efficiently transfer the capabilities of pre-trained transformers into a performant linear attention architecture. LAWCAT integrates causal Conv1D layers to enhance local dependency modeling and employs normalized gated linear attention to improve generalization across varying context lengths. Our comprehensive evaluations demonstrate that, distilling Mistral-7B with only 1K-length sequences yields over 90\% passkey retrieval accuracy up to 22K tokens, significantly extending its effective context window. Similarly, Llama3.2-1B LAWCAT variant achieves competitive performance on S-NIAH 1\&2\&3 tasks (1K-8K context length) and BABILong benchmark (QA2\&amp;QA3, 0K-16K context length), requiring less than 0.1\% pre-training tokens compared with pre-training models. Furthermore, LAWCAT exhibits faster prefill speeds than FlashAttention-2 for sequences exceeding 8K tokens. LAWCAT thus provides an efficient pathway to high-performance, long-context linear models suitable for edge deployment, reducing reliance on extensive long-sequence training data and computational resources.

## 📝 요약

LAWCAT은 긴 문맥 애플리케이션에서 발생하는 변환기 아키텍처의 계산 복잡성을 해결하기 위해 제안된 새로운 선형화 프레임워크입니다. 이 방법은 사전 훈련된 변환기의 능력을 선형 주의 아키텍처로 효율적으로 전이시키며, Conv1D 레이어를 통합하여 지역 의존성 모델링을 강화하고, 정규화된 게이트 선형 주의를 사용하여 다양한 문맥 길이에 대한 일반화를 개선합니다. Mistral-7B를 1K 길이의 시퀀스로 증류하면 22K 토큰까지 90% 이상의 패스키 검색 정확도를 달성하고, Llama3.2-1B LAWCAT 변형은 S-NIAH 및 BABILong 벤치마크에서 경쟁력 있는 성능을 보입니다. 또한, 8K 토큰을 초과하는 시퀀스에서 FlashAttention-2보다 빠른 속도를 제공합니다. LAWCAT은 긴 문맥 선형 모델의 효율적인 경로를 제공하여 엣지 배포에 적합하며, 긴 시퀀스 훈련 데이터와 계산 자원에 대한 의존성을 줄입니다.

## 🎯 주요 포인트

- 1. LAWCAT은 사전 학습된 트랜스포머의 능력을 효율적으로 선형 주의 아키텍처로 전이시키기 위한 새로운 선형화 프레임워크입니다.
- 2. LAWCAT은 인과적 Conv1D 레이어를 통합하여 지역적 의존성 모델링을 강화하고, 정규화된 게이트 선형 주의를 사용하여 다양한 문맥 길이에 대한 일반화를 개선합니다.
- 3. Mistral-7B를 1K 길이의 시퀀스로 증류한 결과, 22K 토큰까지 90% 이상의 패스키 검색 정확도를 달성하였습니다.
- 4. LAWCAT은 8K 이상의 시퀀스에 대해 FlashAttention-2보다 빠른 프리필 속도를 보이며, 엣지 배포에 적합한 고성능 장기 문맥 선형 모델을 제공합니다.
- 5. Llama3.2-1B LAWCAT 변형은 S-NIAH 및 BABILong 벤치마크에서 경쟁력 있는 성능을 보이며, 사전 학습 모델 대비 0.1% 미만의 사전 학습 토큰만을 필요로 합니다.


---

*Generated on 2025-09-24 13:50:10*