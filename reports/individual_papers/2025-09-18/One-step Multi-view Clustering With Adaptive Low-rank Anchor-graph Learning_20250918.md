---
keywords:
  - Adaptive Low-Rank Learning
  - Multi-View Clustering
  - Nuclear Norm-Based Learning
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:17:17.873387",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Adaptive Low-Rank Learning",
    "Multi-View Clustering",
    "Nuclear Norm-Based Learning"
  ],
  "rejected_keywords": [
    "Clustering Optimization"
  ],
  "similarity_scores": {
    "Adaptive Low-Rank Learning": 0.8,
    "Multi-View Clustering": 0.78,
    "Nuclear Norm-Based Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# One-step Multi-view Clustering With Adaptive Low-rank Anchor-graph Learning

**Korean Title:** 단계적 다중 뷰 클러스터링을 위한 적응형 저차원 앵커 그래프 학습

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Adaptive Low-Rank Learning|adaptive low-rank anchor-graph learning]], [[keywords/Multi-View Clustering|anchor graph-based multi-view clustering]], [[keywords/Nuclear Norm-Based Learning|nuclear norm-based adaptive CAG learning model]]

## 🔗 유사한 논문
- [[Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods Reviving Transformer for Graph Clustering]] (82.4% similar)
- [[Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (79.8% similar)
- [[Omni-CLST_ Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering_20250918|Omni-CLST Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering]] (78.7% similar)
- [[Multi-CAP_ A Multi-Robot Connectivity-Aware Hierarchical Coverage Path Planning Algorithm for Unknown Environments_20250919|Multi-CAP A Multi-Robot Connectivity-Aware Hierarchical Coverage Path Planning Algorithm for Unknown Environments]] (78.5% similar)
- [[MemEvo_ Memory-Evolving Incremental Multi-view Clustering_20250919|MemEvo Memory-Evolving Incremental Multi-view Clustering]] (78.2% similar)

## 📋 저자 정보

**Authors:** Zhiyuan Xue, Ben Yang, Xuetao Zhang, Fei Wang, Zhiping Lin

## 📄 Abstract (원문)

In light of their capability to capture structural information while reducing
computing complexity, anchor graph-based multi-view clustering (AGMC) methods
have attracted considerable attention in large-scale clustering problems.
Nevertheless, existing AGMC methods still face the following two issues: 1)
They directly embedded diverse anchor graphs into a consensus anchor graph
(CAG), and hence ignore redundant information and numerous noises contained in
these anchor graphs, leading to a decrease in clustering effectiveness; 2) They
drop effectiveness and efficiency due to independent post-processing to acquire
clustering indicators. To overcome the aforementioned issues, we deliver a
novel one-step multi-view clustering method with adaptive low-rank anchor-graph
learning (OMCAL). To construct a high-quality CAG, OMCAL provides a nuclear
norm-based adaptive CAG learning model against information redundancy and noise
interference. Then, to boost clustering effectiveness and efficiency
substantially, we incorporate category indicator acquisition and CAG learning
into a unified framework. Numerous studies conducted on ordinary and
large-scale datasets indicate that OMCAL outperforms existing state-of-the-art
methods in terms of clustering effectiveness and efficiency.

## 🔍 Abstract (한글 번역)

다음 텍스트를 한국어로 번역하겠습니다. 학문적 어조와 기술 용어를 적절히 유지하겠습니다.

구조적 정보를 포착하면서 계산 복잡성을 줄일 수 있는 능력 덕분에, 앵커 그래프 기반 다중 뷰 클러스터링(AGMC) 방법은 대규모 클러스터링 문제에서 상당한 주목을 받고 있습니다. 그럼에도 불구하고, 기존의 AGMC 방법은 여전히 다음 두 가지 문제에 직면해 있습니다: 1) 다양한 앵커 그래프를 직접적으로 합의 앵커 그래프(CAG)에 내장하여, 이러한 앵커 그래프에 포함된 중복 정보와 많은 잡음을 무시하게 되어 클러스터링 효과가 감소합니다; 2) 클러스터링 지표를 얻기 위한 독립적인 후처리로 인해 효과성과 효율성이 떨어집니다. 위의 문제를 극복하기 위해, 우리는 적응형 저랭크 앵커 그래프 학습(OMCAL)을 통한 새로운 일단계 다중 뷰 클러스터링 방법을 제안합니다. 고품질의 CAG를 구축하기 위해, OMCAL은 정보 중복성과 잡음 간섭에 대응하는 핵 노름 기반 적응형 CAG 학습 모델을 제공합니다. 그런 다음, 클러스터링 효과성과 효율성을 크게 향상시키기 위해, 우리는 범주 지표 획득과 CAG 학습을 통합된 프레임워크에 포함시킵니다. 일반 및 대규모 데이터셋에서 수행된 수많은 연구는 OMCAL이 클러스터링 효과성과 효율성 측면에서 기존의 최첨단 방법들을 능가함을 나타냅니다.

## 📝 요약

이 논문은 대규모 클러스터링 문제에서 구조적 정보를 효과적으로 포착하면서 계산 복잡성을 줄이는 앵커 그래프 기반 다중 뷰 클러스터링(AGMC) 방법의 한계를 극복하기 위해 새로운 방법론을 제안합니다. 기존 AGMC 방법은 다양한 앵커 그래프를 통합하는 과정에서 정보 중복과 노이즈를 무시하여 클러스터링 효과가 감소하고, 독립적인 후처리로 인해 효율성이 떨어지는 문제가 있었습니다. 이를 해결하기 위해, 본 연구는 적응형 저랭크 앵커 그래프 학습을 활용한 새로운 단일 단계 다중 뷰 클러스터링 방법(OMCAL)을 제안합니다. OMCAL은 정보 중복과 노이즈를 줄이기 위해 핵심 노름 기반의 적응형 CAG 학습 모델을 사용하며, 클러스터링 지표 획득과 CAG 학습을 통합된 프레임워크로 결합하여 효율성을 크게 향상시킵니다. 실험 결과, OMCAL은 기존 최첨단 방법들보다 클러스터링 효과와 효율성 면에서 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 앵커 그래프 기반 다중 뷰 클러스터링(AGMC) 방법은 구조적 정보를 포착하면서 계산 복잡성을 줄이는 데 주목받고 있다.

- 2. 기존 AGMC 방법은 다양한 앵커 그래프를 합의 앵커 그래프(CAG)로 직접 내장하여 중복 정보와 잡음을 무시하는 문제가 있다.

- 3. OMCAL은 정보 중복과 잡음 간섭에 대응하기 위해 핵심 노름 기반의 적응형 CAG 학습 모델을 제공한다.

- 4. OMCAL은 카테고리 지표 획득과 CAG 학습을 통합된 프레임워크로 결합하여 클러스터링 효과성과 효율성을 크게 향상시킨다.

- 5. 일반 및 대규모 데이터셋에 대한 연구에서 OMCAL은 기존 최신 방법들보다 클러스터링 효과성과 효율성에서 뛰어난 성능을 보인다.

---

*Generated on 2025-09-20 05:44:28*