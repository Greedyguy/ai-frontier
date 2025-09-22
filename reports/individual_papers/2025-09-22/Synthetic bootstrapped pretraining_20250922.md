# Synthetic bootstrapped pretraining

**Korean Title:** 합성 부트스트랩 사전 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Bayesian Interpretation in Pretraining

## 🔗 유사한 논문
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (80.6% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (78.5% similar)
- [[2025-09-19/From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery Reinforced Distillation of Large Language Model Agents]] (78.5% similar)
- [[2025-09-18/Self-Improving Embodied Foundation Models_20250918|Self-Improving Embodied Foundation Models]] (78.5% similar)
- [[2025-09-18/Patent Language Model Pretraining with ModernBERT_20250918|Patent Language Model Pretraining with ModernBERT]] (77.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15248v1 Announce Type: cross 
Abstract: We introduce Synthetic Bootstrapped Pretraining (SBP), a language model (LM) pretraining procedure that first learns a model of relations between documents from the pretraining dataset and then leverages it to synthesize a vast new corpus for joint training. While the standard pretraining teaches LMs to learn causal correlations among tokens within a single document, it is not designed to efficiently model the rich, learnable inter-document correlations that can potentially lead to better performance. We validate SBP by designing a compute-matched pretraining setup and pretrain a 3B-parameter model on up to 1T tokens from scratch. We find SBP consistently improves upon a strong repetition baseline and delivers a significant fraction of performance improvement attainable by an oracle upper bound with access to 20x more unique data. Qualitative analysis reveals that the synthesized documents go beyond mere paraphrases -- SBP first abstracts a core concept from the seed material and then crafts a new narration on top of it. Besides strong empirical performance, SBP admits a natural Bayesian interpretation: the synthesizer implicitly learns to abstract the latent concepts shared between related documents.

## 🔍 Abstract (한글 번역)

arXiv:2509.15248v1 발표 유형: 교차  
요약: 우리는 문서들 간의 관계를 사전 학습 데이터셋에서 학습한 후, 이를 활용하여 공동 학습을 위한 방대한 새로운 코퍼스를 합성하는 언어 모델(LM) 사전 학습 절차인 Synthetic Bootstrapped Pretraining (SBP)을 소개합니다. 표준 사전 학습은 LMs가 단일 문서 내에서 토큰 간의 인과적 상관관계를 학습하도록 가르치지만, 이는 더 나은 성능을 이끌어낼 수 있는 풍부하고 학습 가능한 문서 간 상관관계를 효율적으로 모델링하도록 설계되지 않았습니다. 우리는 계산이 일치하는 사전 학습 설정을 설계하고, 1조 개의 토큰에 대해 처음부터 3B-파라미터 모델을 사전 학습하여 SBP를 검증합니다. SBP는 강력한 반복 기준선보다 일관되게 개선을 이루며, 20배 더 많은 고유 데이터를 액세스할 수 있는 오라클 상한선이 달성할 수 있는 성능 향상의 상당 부분을 제공합니다. 질적 분석을 통해 합성된 문서들이 단순한 패러프레이즈를 넘어서는 것을 확인할 수 있습니다. SBP는 먼저 시드 자료에서 핵심 개념을 추상화한 후, 이를 바탕으로 새로운 서술을 만듭니다. 강력한 경험적 성능 외에도, SBP는 자연스러운 베이지안 해석을 허용합니다: 합성기는 관련 문서들 간에 공유되는 잠재 개념을 추상적으로 학습합니다.

## 📝 요약

Synthetic Bootstrapped Pretraining(SBP)은 문서 간 관계를 학습하여 새로운 대규모 코퍼스를 생성하고 이를 통해 언어 모델을 사전 학습하는 방법입니다. 기존 사전 학습은 문서 내 토큰 간 인과 관계에 집중하지만, SBP는 문서 간 상관관계를 효율적으로 모델링하여 성능을 향상시킵니다. 3B-파라미터 모델을 1조 토큰으로 학습한 결과, SBP는 반복 기반 모델보다 성능이 향상되었으며, 20배 많은 데이터에 접근할 수 있는 이상적 상한선의 상당 부분을 달성했습니다. SBP는 문서의 핵심 개념을 추상화하고 새로운 서술을 생성하며, 베이지안 해석이 가능합니다.

## 🎯 주요 포인트

- 1. Synthetic Bootstrapped Pretraining(SBP)는 문서 간 관계를 모델링하여 새로운 대규모 코퍼스를 합성하고 이를 공동 학습에 활용하는 언어 모델 사전 학습 절차입니다.

- 2. SBP는 단일 문서 내의 인과적 상관관계 학습을 넘어서, 문서 간의 풍부한 상관관계를 효율적으로 모델링하여 성능 향상을 도모합니다.

- 3. SBP를 통해 3B-파라미터 모델을 최대 1조 개의 토큰으로 사전 학습한 결과, 강력한 반복 기준선을 지속적으로 개선하고, 20배 더 많은 고유 데이터를 가진 경우에 도달할 수 있는 성능 향상의 상당 부분을 제공합니다.

- 4. SBP로 합성된 문서는 단순한 패러프레이즈를 넘어서, 핵심 개념을 추상화하고 이를 바탕으로 새로운 서술을 만들어냅니다.

- 5. SBP는 관련 문서 간에 공유되는 잠재 개념을 추상화하는 학습을 통해 자연스러운 베이지안 해석을 허용합니다.

---

*Generated on 2025-09-22 13:48:57*