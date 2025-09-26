<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:23:17.068089",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Articulator-based Disentanglement",
    "Channel-aware Regularization",
    "Non-autoregressive Transformer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.78,
    "Articulator-based Disentanglement": 0.82,
    "Channel-aware Regularization": 0.79,
    "Non-autoregressive Transformer": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer-based sign language production",
        "canonical": "Transformer",
        "aliases": [
          "Transformer-based SLP"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are crucial for understanding the architecture used in the framework, linking to broader technical concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Articulator-based disentanglement",
        "canonical": "Articulator-based Disentanglement",
        "aliases": [
          "Articulator Disentanglement"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach specific to the paper's methodology, offering a unique perspective on disentanglement strategies.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Channel-aware regularization",
        "canonical": "Channel-aware Regularization",
        "aliases": [
          "Channel Regularization"
        ],
        "category": "unique_technical",
        "rationale": "This technique is specific to the paper and crucial for understanding the regularization process used in the model.",
        "novelty_score": 0.68,
        "connectivity_score": 0.58,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "Non-autoregressive transformer decoder",
        "canonical": "Non-autoregressive Transformer",
        "aliases": [
          "Non-autoregressive Decoder"
        ],
        "category": "specific_connectable",
        "rationale": "This variant of transformer architecture is significant for understanding the model's decoding process.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "gloss-free",
      "state-of-the-art"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer-based sign language production",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Articulator-based disentanglement",
      "resolved_canonical": "Articulator-based Disentanglement",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Channel-aware regularization",
      "resolved_canonical": "Channel-aware Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.58,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Non-autoregressive transformer decoder",
      "resolved_canonical": "Non-autoregressive Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Disentangle and Regularize: Sign Language Production with Articulator-Based Disentanglement and Channel-Aware Regularization

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2504.06610.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2504.06610](https://arxiv.org/abs/2504.06610)

## 🔗 유사한 논문
- [[2025-09-19/Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production_20250919|Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production]] (88.3% similar)
- [[2025-09-23/Revisiting Speech-Lip Alignment_ A Phoneme-Aware Speech Encoder for Robust Talking Head Synthesis_20250923|Revisiting Speech-Lip Alignment: A Phoneme-Aware Speech Encoder for Robust Talking Head Synthesis]] (82.0% similar)
- [[2025-09-23/Inceptive Transformers_ Enhancing Contextual Representations through Multi-Scale Feature Learning Across Domains and Languages_20250923|Inceptive Transformers: Enhancing Contextual Representations through Multi-Scale Feature Learning Across Domains and Languages]] (81.6% similar)
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (81.6% similar)
- [[2025-09-17/SSL-SSAW_ Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation_20250917|SSL-SSAW: Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Non-autoregressive Transformer|Non-autoregressive Transformer]]
**⚡ Unique Technical**: [[keywords/Articulator-based Disentanglement|Articulator-based Disentanglement]], [[keywords/Channel-aware Regularization|Channel-aware Regularization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.06610v3 Announce Type: replace 
Abstract: In this work, we propose DARSLP, a simple gloss-free, transformer-based sign language production (SLP) framework that directly maps spoken-language text to sign pose sequences. We first train a pose autoencoder that encodes sign poses into a compact latent space using an articulator-based disentanglement strategy, where features corresponding to the face, right hand, left hand, and body are modeled separately to promote structured and interpretable representation learning. Next, a non-autoregressive transformer decoder is trained to predict these latent representations from word-level text embeddings of the input sentence. To guide this process, we apply channel-aware regularization by aligning predicted latent distributions with priors extracted from the ground-truth encodings using a KL divergence loss. The contribution of each channel to the loss is weighted according to its associated articulator region, enabling the model to account for the relative importance of different articulators during training. Our approach does not rely on gloss supervision or pretrained models, and achieves state-of-the-art results on the PHOENIX14T and CSL-Daily datasets.

## 📝 요약

이 연구에서는 DARSLP라는 간단한 글로스 없이 동작하는 트랜스포머 기반 수어 생성 프레임워크를 제안합니다. 이 프레임워크는 음성 언어 텍스트를 수어 자세 시퀀스로 직접 변환합니다. 먼저, 얼굴, 오른손, 왼손, 몸을 각각 모델링하여 구조적이고 해석 가능한 표현 학습을 촉진하는 자세 오토인코더를 훈련합니다. 이후, 비자기회귀 트랜스포머 디코더를 사용하여 입력 문장의 단어 수준 텍스트 임베딩에서 이러한 잠재 표현을 예측합니다. 예측된 잠재 분포를 실제 인코딩에서 추출한 사전 분포와 정렬하기 위해 채널 인식 정규화를 적용하며, KL 발산 손실을 사용합니다. 각 채널의 손실 기여도는 관련 관절 부위에 따라 가중치가 부여되어 훈련 중 다양한 관절의 상대적 중요성을 고려합니다. 이 방법은 글로스 감독이나 사전 학습된 모델에 의존하지 않으며, PHOENIX14T 및 CSL-Daily 데이터셋에서 최첨단 성능을 달성합니다.

## 🎯 주요 포인트

- 1. DARSLP는 구어 텍스트를 수어 자세 시퀀스로 직접 변환하는 글로스 없는 트랜스포머 기반 수어 생성 프레임워크입니다.
- 2. 포즈 오토인코더는 얼굴, 오른손, 왼손, 몸의 특징을 별도로 모델링하여 구조적이고 해석 가능한 표현 학습을 촉진합니다.
- 3. 비자기회귀 트랜스포머 디코더는 입력 문장의 단어 수준 텍스트 임베딩으로부터 잠재 표현을 예측하도록 훈련됩니다.
- 4. 채널 인식 정규화를 통해 예측된 잠재 분포를 실제 인코딩에서 추출한 사전 분포와 정렬하여 학습을 유도합니다.
- 5. 이 접근 방식은 글로스 감독이나 사전 훈련된 모델에 의존하지 않으며, PHOENIX14T 및 CSL-Daily 데이터셋에서 최첨단 결과를 달성합니다.


---

*Generated on 2025-09-24 15:23:17*