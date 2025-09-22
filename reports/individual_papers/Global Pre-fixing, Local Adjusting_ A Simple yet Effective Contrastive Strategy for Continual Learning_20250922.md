# Global Pre-fixing, Local Adjusting: A Simple yet Effective Contrastive Strategy for Continual Learning

**Korean Title:** 글로벌 사전 고정, 로컬 조정: 연속 학습을 위한 간단하지만 효과적인 대조 전략

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Equiangular Tight Frame

## 🔗 유사한 논문
- [[2025-09-18/HAM_ Hierarchical Adapter Merging for Scalable Continual Learning_20250918|HAM Hierarchical Adapter Merging for Scalable Continual Learning]] (82.7% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (81.7% similar)
- [[2025-09-19/ToolSample_ Dual Dynamic Sampling Methods with Curriculum Learning for RL-based Tool Learning_20250919|ToolSample Dual Dynamic Sampling Methods with Curriculum Learning for RL-based Tool Learning]] (81.1% similar)
- [[2025-09-22/RegionMed-CLIP_ A Region-Aware Multimodal Contrastive Learning Pre-trained Model for Medical Image Understanding_20250922|RegionMed-CLIP A Region-Aware Multimodal Contrastive Learning Pre-trained Model for Medical Image Understanding]] (80.6% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (80.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15347v1 Announce Type: new 
Abstract: Continual learning (CL) involves acquiring and accumulating knowledge from evolving tasks while alleviating catastrophic forgetting. Recently, leveraging contrastive loss to construct more transferable and less forgetful representations has been a promising direction in CL. Despite advancements, their performance is still limited due to confusion arising from both inter-task and intra-task features. To address the problem, we propose a simple yet effective contrastive strategy named \textbf{G}lobal \textbf{P}re-fixing, \textbf{L}ocal \textbf{A}djusting for \textbf{S}upervised \textbf{C}ontrastive learning (GPLASC). Specifically, to avoid task-level confusion, we divide the entire unit hypersphere of representations into non-overlapping regions, with the centers of the regions forming an inter-task pre-fixed \textbf{E}quiangular \textbf{T}ight \textbf{F}rame (ETF). Meanwhile, for individual tasks, our method helps regulate the feature structure and form intra-task adjustable ETFs within their respective allocated regions. As a result, our method \textit{simultaneously} ensures discriminative feature structures both between tasks and within tasks and can be seamlessly integrated into any existing contrastive continual learning framework. Extensive experiments validate its effectiveness.

## 🔍 Abstract (한글 번역)

arXiv:2509.15347v1 발표 유형: 신규  
초록: 연속 학습(CL)은 진화하는 과제로부터 지식을 습득하고 축적하면서도 치명적인 망각을 완화하는 것을 포함합니다. 최근에는 대조 손실을 활용하여 더 전이 가능하고 덜 망각하는 표현을 구축하는 것이 CL에서 유망한 방향으로 떠오르고 있습니다. 그러나 발전에도 불구하고, 이들의 성능은 여전히 과제 간 및 과제 내 특징에서 발생하는 혼란으로 인해 제한적입니다. 이 문제를 해결하기 위해, 우리는 \textbf{G}lobal \textbf{P}re-fixing, \textbf{L}ocal \textbf{A}djusting for \textbf{S}upervised \textbf{C}ontrastive learning (GPLASC)라는 간단하면서도 효과적인 대조 전략을 제안합니다. 구체적으로, 과제 수준의 혼란을 피하기 위해, 우리는 표현의 전체 단위 초구를 겹치지 않는 영역으로 나누고, 이 영역의 중심이 과제 간 고정된 \textbf{E}quiangular \textbf{T}ight \textbf{F}rame (ETF)을 형성합니다. 한편, 개별 과제에 대해서는, 우리의 방법이 특징 구조를 조절하고 할당된 각 영역 내에서 과제 내 조정 가능한 ETF를 형성하도록 돕습니다. 결과적으로, 우리의 방법은 \textit{동시에} 과제 간 및 과제 내에서 변별적인 특징 구조를 보장하며, 기존의 어떤 대조 연속 학습 프레임워크에도 매끄럽게 통합될 수 있습니다. 광범위한 실험을 통해 그 효과가 검증되었습니다.

## 📝 요약

이 논문은 지속 학습(CL)에서 발생하는 문제인 망각을 줄이기 위해 대조 손실을 활용하는 새로운 방법론을 제안합니다. 기존 방법들은 과제 간 및 과제 내 특징의 혼란으로 인해 성능이 제한적이었습니다. 이를 해결하기 위해, 저자들은 \textbf{G}lobal \textbf{P}re-fixing, \textbf{L}ocal \textbf{A}djusting for \textbf{S}upervised \textbf{C}ontrastive learning (GPLASC)라는 간단하면서도 효과적인 대조 전략을 제안합니다. 이 방법은 표현의 전체 단위 초구를 비중첩 영역으로 나누고, 영역의 중심을 과제 간 고정된 \textbf{E}quiangular \textbf{T}ight \textbf{F}rame (ETF)로 형성하여 과제 수준의 혼란을 피합니다. 개별 과제에 대해서는, 과제 내 조정 가능한 ETF를 형성하여 특징 구조를 조절합니다. 이로 인해 과제 간 및 과제 내에서 동시에 구별 가능한 특징 구조를 보장하며, 기존의 대조 지속 학습 프레임워크에 원활하게 통합될 수 있습니다. 광범위한 실험을 통해 이 방법의 효과가 검증되었습니다.

## 🎯 주요 포인트

- 1. 지속 학습(CL)은 진화하는 작업에서 지식을 획득하고 누적하면서 망각을 완화하는 것을 목표로 합니다.

- 2. 대조 손실을 활용하여 더 전이 가능하고 덜 망각하는 표현을 구축하는 것이 CL에서 유망한 방향으로 떠오르고 있습니다.

- 3. 글로벌 고정 및 로컬 조정을 통한 감독 대조 학습(GPLASC) 전략을 제안하여 작업 간 및 작업 내 특징 혼란 문제를 해결합니다.

- 4. 제안된 방법은 표현의 전체 단위 초구를 비중첩 영역으로 나누고, 영역의 중심을 통해 작업 간 고정된 등각 타이트 프레임(ETF)을 형성합니다.

- 5. 제안된 방법은 기존의 대조 지속 학습 프레임워크에 원활하게 통합될 수 있으며, 광범위한 실험을 통해 그 효과가 검증되었습니다.

---

*Generated on 2025-09-22 15:10:43*