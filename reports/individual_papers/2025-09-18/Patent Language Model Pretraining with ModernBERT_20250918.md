---
keywords:
  - Transformer Architecture
  - Natural Language Processing
  - Patent NLP
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:16:42.397070",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer Architecture",
    "Natural Language Processing",
    "Patent NLP"
  ],
  "rejected_keywords": [
    "FlashAttention",
    "Domain-specific Pretraining"
  ],
  "similarity_scores": {
    "Transformer Architecture": 0.8,
    "Natural Language Processing": 0.75,
    "Patent NLP": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Patent Language Model Pretraining with ModernBERT

**Korean Title:** 특허 언어 모델 사전 훈련: ModernBERT 활용

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]     [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**🔗 Specific Connectable**: [[keywords/Transformer Architecture|Transformer-based language models]]
**⚡ Unique Technical**: [[keywords/Patent NLP|Patent-focused NLP tasks]]

## 🔗 유사한 논문
- [[BERTector_ An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model_20250918|BERTector An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model]] (79.7% similar)
- [[FroM_ Frobenius Norm-Based Data-Free Adaptive Model Merging_20250918|FroM Frobenius Norm-Based Data-Free Adaptive Model Merging]] (78.5% similar)
- [[Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (78.4% similar)
- [[WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (78.3% similar)
- [[Self-Improving Embodied Foundation Models_20250918|Self-Improving Embodied Foundation Models]] (77.9% similar)

## 📋 저자 정보

**Authors:** Amirhossein Yousefiramandi, Ciaran Cooney

## 📄 Abstract (원문)

Transformer-based language models such as BERT have become foundational in
NLP, yet their performance degrades in specialized domains like patents, which
contain long, technical, and legally structured text. Prior approaches to
patent NLP have primarily relied on fine-tuning general-purpose models or
domain-adapted variants pretrained with limited data. In this work, we pretrain
3 domain-specific masked language models for patents, using the ModernBERT
architecture and a curated corpus of over 60 million patent records. Our
approach incorporates architectural optimizations, including FlashAttention,
rotary embeddings, and GLU feed-forward layers. We evaluate our models on four
downstream patent classification tasks. Our model, ModernBERT-base-PT,
consistently outperforms the general-purpose ModernBERT baseline on three out
of four datasets and achieves competitive performance with a baseline
PatentBERT. Additional experiments with ModernBERT-base-VX and
Mosaic-BERT-large demonstrate that scaling the model size and customizing the
tokenizer further enhance performance on selected tasks. Notably, all
ModernBERT variants retain substantially faster inference over - 3x that of
PatentBERT - underscoring their suitability for time-sensitive applications.
These results underscore the benefits of domain-specific pretraining and
architectural improvements for patent-focused NLP tasks.

## 🔍 Abstract (한글 번역)

트랜스포머 기반의 언어 모델, 예를 들어 BERT는 자연어 처리(NLP)에서 기본적인 역할을 하고 있지만, 특허와 같이 길고 기술적이며 법적으로 구조화된 텍스트를 포함하는 전문 분야에서는 성능이 저하됩니다. 이전의 특허 NLP 접근법은 주로 일반 목적의 모델을 미세 조정하거나 제한된 데이터로 사전 학습된 도메인 적응 변형에 의존해 왔습니다. 본 연구에서는 ModernBERT 아키텍처와 6천만 건 이상의 특허 기록으로 구성된 큐레이션된 코퍼스를 사용하여 특허를 위한 3개의 도메인 특화 마스크 언어 모델을 사전 학습합니다. 우리의 접근법은 FlashAttention, 회전 임베딩, GLU 피드포워드 레이어를 포함한 아키텍처 최적화를 통합합니다. 우리는 네 가지 다운스트림 특허 분류 작업에서 우리의 모델을 평가합니다. 우리의 모델인 ModernBERT-base-PT는 네 개의 데이터셋 중 세 개에서 일반 목적의 ModernBERT 기준 모델을 일관되게 능가하며, 기준 모델인 PatentBERT와 경쟁력 있는 성능을 달성합니다. ModernBERT-base-VX 및 Mosaic-BERT-large와의 추가 실험은 모델 크기를 확장하고 토크나이저를 맞춤화하는 것이 선택된 작업에서 성능을 더욱 향상시킨다는 것을 보여줍니다. 특히, 모든 ModernBERT 변형은 PatentBERT의 3배 이상 빠른 추론 속도를 유지하여 시간 민감한 애플리케이션에 적합함을 강조합니다. 이러한 결과는 특허 중심의 NLP 작업을 위한 도메인 특화 사전 학습과 아키텍처 개선의 이점을 강조합니다.

## 📝 요약

이 연구는 특허 분야의 NLP 작업에 적합한 도메인 특화 마스크드 언어 모델을 개발했습니다. ModernBERT 아키텍처를 기반으로, 6천만 개 이상의 특허 기록을 사용하여 세 가지 모델을 사전 훈련했습니다. FlashAttention, 회전 임베딩, GLU 피드포워드 레이어 등 아키텍처 최적화를 적용했습니다. 네 가지 특허 분류 작업에서 평가한 결과, ModernBERT-base-PT 모델은 일반적인 ModernBERT보다 우수한 성능을 보였으며, PatentBERT와도 경쟁력 있는 성능을 나타냈습니다. 모델 크기 확장과 토크나이저 맞춤화는 성능을 더욱 향상시켰으며, 모든 ModernBERT 변형 모델은 PatentBERT보다 3배 빠른 추론 속도를 유지했습니다. 이는 특허 중심 NLP 작업에서 도메인 특화 사전 훈련과 아키텍처 개선의 이점을 강조합니다.

## 🎯 주요 포인트

- 1. 특허 분야의 NLP 작업에서 도메인 특화 사전 학습과 아키텍처 개선의 이점이 강조되었습니다.

- 2. ModernBERT 아키텍처를 기반으로 한 3개의 도메인 특화 마스크드 언어 모델이 개발되었습니다.

- 3. ModernBERT-base-PT 모델은 4개의 특허 분류 작업 중 3개에서 일반 목적의 ModernBERT보다 우수한 성능을 보였습니다.

- 4. 모델 크기 확장과 토크나이저 맞춤화가 특정 작업에서 성능을 향상시키는 것으로 나타났습니다.

- 5. 모든 ModernBERT 변형 모델은 PatentBERT보다 3배 빠른 추론 속도를 유지하여 시간 민감형 응용에 적합합니다.

---

*Generated on 2025-09-20 02:43:07*