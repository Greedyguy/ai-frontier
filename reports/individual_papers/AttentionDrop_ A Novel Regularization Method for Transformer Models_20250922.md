# AttentionDrop: A Novel Regularization Method for Transformer Models

**Korean Title:** 어텐션드롭: 트랜스포머 모델을 위한 새로운 정규화 기법

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Stochastic Regularization Techniques

## 🔗 유사한 논문
- [[2025-09-22/Attention Schema-based Attention Control (ASAC)_ A Cognitive-Inspired Approach for Attention Management in Transformers_20250922|Attention Schema-based Attention Control (ASAC) A Cognitive-Inspired Approach for Attention Management in Transformers]] (81.9% similar)
- [[2025-09-22/Hierarchical Self-Attention_ Generalizing Neural Attention Mechanics to Multi-Scale Problems_20250922|Hierarchical Self-Attention Generalizing Neural Attention Mechanics to Multi-Scale Problems]] (81.0% similar)
- [[2025-09-19/Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (80.0% similar)
- [[2025-09-19/Value-Guided KV Compression for LLMs via Approximated CUR Decomposition_20250919|Value-Guided KV Compression for LLMs via Approximated CUR Decomposition]] (80.0% similar)
- [[2025-09-18/Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods Reviving Transformer for Graph Clustering]] (80.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.12088v2 Announce Type: replace-cross 
Abstract: Transformer-based architectures achieve state-of-the-art performance across a wide range of tasks in natural language processing, computer vision, and speech processing. However, their immense capacity often leads to overfitting, especially when training data is limited or noisy. In this research, a unified family of stochastic regularization techniques has been proposed, i.e. AttentionDrop with its three different variants, which operate directly on the self-attention distributions. Hard Attention Masking randomly zeroes out top-k attention logits per query to encourage diverse context utilization, Blurred Attention Smoothing applies a dynamic Gaussian convolution over attention logits to diffuse overly peaked distributions, and Consistency-Regularized AttentionDrop enforces output stability under multiple independent AttentionDrop perturbations via a KL-based consistency loss. Results achieved in the study demonstrate that AttentionDrop consistently improves accuracy, calibration, and adversarial robustness over standard Dropout, DropConnect, and R-Drop baselines

## 🔍 Abstract (한글 번역)

arXiv:2504.12088v2 발표 유형: 교체-크로스  
초록: 트랜스포머 기반 아키텍처는 자연어 처리, 컴퓨터 비전, 음성 처리 등 다양한 작업에서 최첨단 성능을 달성하고 있습니다. 그러나 이들의 엄청난 용량은 종종 과적합을 초래하며, 특히 훈련 데이터가 제한적이거나 잡음이 많은 경우에 그러합니다. 본 연구에서는 자기 주의 분포에 직접 작용하는 세 가지 변형을 가진 AttentionDrop이라는 통합된 확률적 정규화 기법을 제안하였습니다. Hard Attention Masking은 쿼리당 상위 k개의 주의 로그잇을 무작위로 0으로 만들어 다양한 문맥 활용을 촉진하며, Blurred Attention Smoothing은 과도하게 뾰족한 분포를 확산시키기 위해 주의 로그잇에 동적 가우시안 컨볼루션을 적용합니다. 또한, Consistency-Regularized AttentionDrop은 KL 기반의 일관성 손실을 통해 여러 독립적인 AttentionDrop 변동 하에서 출력의 안정성을 강화합니다. 연구 결과, AttentionDrop은 표준 드롭아웃(Dropout), 드롭커넥트(DropConnect), R-Drop 기준선에 비해 정확도, 보정, 적대적 견고성을 일관되게 향상시킵니다.

## 📝 요약

이 연구는 자연어 처리, 컴퓨터 비전, 음성 처리에서 뛰어난 성능을 보이는 트랜스포머 기반 아키텍처의 과적합 문제를 해결하기 위해 새로운 확률적 정규화 기법인 AttentionDrop을 제안합니다. AttentionDrop은 셀프 어텐션 분포에 직접 작용하며, 세 가지 변형을 포함합니다. Hard Attention Masking은 다양한 문맥 활용을 위해 특정 쿼리의 상위 k개의 어텐션 로짓을 무작위로 0으로 설정하고, Blurred Attention Smoothing은 동적 가우시안 합성을 통해 과도하게 집중된 분포를 확산시킵니다. Consistency-Regularized AttentionDrop은 KL 기반의 일관성 손실을 통해 여러 독립적인 AttentionDrop 변형에서 출력의 안정성을 강화합니다. 연구 결과, AttentionDrop은 기존의 Dropout, DropConnect, R-Drop 대비 정확성, 보정, 적대적 견고성을 일관되게 향상시킵니다.

## 🎯 주요 포인트

- 1. Transformer 기반 아키텍처는 자연어 처리, 컴퓨터 비전, 음성 처리 등 다양한 작업에서 최첨단 성능을 발휘하지만, 데이터가 제한적이거나 노이즈가 많은 경우 과적합이 발생할 수 있습니다.

- 2. 본 연구에서는 자기 주의 분포에 직접 작용하는 세 가지 변형의 AttentionDrop이라는 확률적 정규화 기법을 제안했습니다.

- 3. Hard Attention Masking은 쿼리당 상위 k개의 주의 로그잇을 무작위로 0으로 만들어 다양한 문맥 활용을 촉진합니다.

- 4. Blurred Attention Smoothing은 동적 가우시안 컨볼루션을 통해 지나치게 뾰족한 분포를 확산시킵니다.

- 5. Consistency-Regularized AttentionDrop은 KL 기반의 일관성 손실을 통해 여러 독립적인 AttentionDrop 변동에서 출력의 안정성을 강화합니다.

---

*Generated on 2025-09-22 14:46:33*