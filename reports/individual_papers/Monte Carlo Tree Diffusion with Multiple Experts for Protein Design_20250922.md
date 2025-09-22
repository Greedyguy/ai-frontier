# Monte Carlo Tree Diffusion with Multiple Experts for Protein Design

**Korean Title:** 단백질 설계를 위한 다중 전문가 기반 몬테카를로 트리 확산

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-expert Selection Rule

## 🔗 유사한 논문
- [[2025-09-18/Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (80.3% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (79.1% similar)
- [[2025-09-19/LEED_ A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning_20250919|LEED A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (79.0% similar)
- [[2025-09-18/Towards universal property prediction in Cartesian space_ TACE is all you need_20250918|Towards universal property prediction in Cartesian space TACE is all you need]] (78.7% similar)
- [[2025-09-19/Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation_20250919|Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation]] (78.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15796v1 Announce Type: cross 
Abstract: The goal of protein design is to generate amino acid sequences that fold into functional structures with desired properties. Prior methods combining autoregressive language models with Monte Carlo Tree Search (MCTS) struggle with long-range dependencies and suffer from an impractically large search space. We propose MCTD-ME, Monte Carlo Tree Diffusion with Multiple Experts, which integrates masked diffusion models with tree search to enable multi-token planning and efficient exploration. Unlike autoregressive planners, MCTD-ME uses biophysical-fidelity-enhanced diffusion denoising as the rollout engine, jointly revising multiple positions and scaling to large sequence spaces. It further leverages experts of varying capacities to enrich exploration, guided by a pLDDT-based masking schedule that targets low-confidence regions while preserving reliable residues. We propose a novel multi-expert selection rule (PH-UCT-ME) extends predictive-entropy UCT to expert ensembles. On the inverse folding task (CAMEO and PDB benchmarks), MCTD-ME outperforms single-expert and unguided baselines in both sequence recovery (AAR) and structural similarity (scTM), with gains increasing for longer proteins and benefiting from multi-expert guidance. More generally, the framework is model-agnostic and applicable beyond inverse folding, including de novo protein engineering and multi-objective molecular generation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15796v1 발표 유형: 교차  
초록: 단백질 설계의 목표는 원하는 특성을 가진 기능적 구조로 접히는 아미노산 서열을 생성하는 것입니다. 이전의 자동회귀 언어 모델과 몬테카를로 트리 탐색(MCTS)을 결합한 방법은 장거리 의존성에서 어려움을 겪고 비현실적으로 큰 탐색 공간을 가지고 있습니다. 우리는 다중 전문가 몬테카를로 트리 확산(MCTD-ME)을 제안하며, 이는 마스킹된 확산 모델을 트리 탐색과 통합하여 다중 토큰 계획 및 효율적인 탐색을 가능하게 합니다. 자동회귀 계획자와 달리, MCTD-ME는 생물물리적 신뢰성이 향상된 확산 복원 엔진을 사용하여 여러 위치를 공동으로 수정하고 큰 서열 공간으로 확장합니다. 또한 다양한 역량을 가진 전문가들을 활용하여 탐색을 풍부하게 하며, 신뢰할 수 있는 잔류물을 보존하면서 낮은 신뢰도 영역을 목표로 하는 pLDDT 기반 마스킹 일정에 의해 안내됩니다. 우리는 예측 엔트로피 UCT를 전문가 앙상블로 확장하는 새로운 다중 전문가 선택 규칙(PH-UCT-ME)을 제안합니다. 역접힘 작업(CAMEO 및 PDB 벤치마크)에서 MCTD-ME는 단일 전문가 및 비유도 기준선보다 서열 회복(AAR) 및 구조적 유사성(scTM)에서 더 나은 성능을 보이며, 긴 단백질에서 이득이 증가하고 다중 전문가 안내의 혜택을 받습니다. 더 일반적으로, 이 프레임워크는 모델에 구애받지 않으며 역접힘을 넘어 새로운 단백질 공학 및 다목적 분자 생성에도 적용 가능합니다.

## 📝 요약

단백질 설계의 목표는 원하는 특성을 가진 기능적 구조로 접히는 아미노산 서열을 생성하는 것입니다. 기존 방법들은 장거리 의존성과 큰 탐색 공간 문제를 겪습니다. 이를 해결하기 위해, 우리는 MCTD-ME(Monte Carlo Tree Diffusion with Multiple Experts)를 제안합니다. 이는 마스크된 확산 모델과 트리 탐색을 결합하여 다중 토큰 계획과 효율적인 탐색을 가능하게 합니다. MCTD-ME는 생물물리학적 정확성을 강화한 확산 복원을 사용하여 여러 위치를 동시에 수정하고 큰 서열 공간에 확장할 수 있습니다. 또한 다양한 전문가를 활용하여 탐색을 풍부하게 하고, pLDDT 기반 마스킹 스케줄을 통해 신뢰도가 낮은 영역을 타겟으로 하면서 신뢰할 수 있는 잔기를 보존합니다. 새로운 다중 전문가 선택 규칙(PH-UCT-ME)을 제안하여 예측 엔트로피 UCT를 전문가 앙상블로 확장합니다. 역접힘 과제(CAMEO 및 PDB 벤치마크)에서 MCTD-ME는 단일 전문가 및 비유도 기준을 초과하는 성능을 보였으며, 특히 긴 단백질에서의 성능 향상과 다중 전문가 지도의 이점을 제공합니다. 이 프레임워크는 모델에 구애받지 않으며, 역접힘 외에도 새로운 단백질 공학 및 다중 목표 분자 생성에 적용할 수 있습니다.

## 🎯 주요 포인트

- 1. MCTD-ME는 마스크된 확산 모델과 트리 탐색을 통합하여 다중 토큰 계획과 효율적인 탐색을 가능하게 합니다.

- 2. MCTD-ME는 생물물리학적 정확성이 향상된 확산 복원 엔진을 사용하여 여러 위치를 동시에 수정하고 큰 시퀀스 공간으로 확장할 수 있습니다.

- 3. 다양한 용량의 전문가를 활용하여 탐색을 풍부하게 하고, 신뢰도가 낮은 영역을 목표로 하면서 신뢰할 수 있는 잔류물을 보존하는 pLDDT 기반 마스킹 스케줄을 사용합니다.

- 4. 새로운 다중 전문가 선택 규칙인 PH-UCT-ME는 예측 엔트로피 UCT를 전문가 앙상블로 확장합니다.

- 5. MCTD-ME는 CAMEO 및 PDB 벤치마크의 역접힘 작업에서 단일 전문가 및 비유도 기준보다 시퀀스 회복과 구조적 유사성에서 더 우수한 성능을 보입니다.

---

*Generated on 2025-09-22 14:11:27*