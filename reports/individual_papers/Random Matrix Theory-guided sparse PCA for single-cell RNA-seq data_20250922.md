# Random Matrix Theory-guided sparse PCA for single-cell RNA-seq data

**Korean Title:** 랜덤 행렬 이론 기반 희소 주성분 분석을 통한 단일 세포 RNA-seq 데이터 분석

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Sparse PCA, Random Matrix Theory

## 🔗 유사한 논문
- [[2025-09-18/Balancing Sparse RNNs with Hyperparameterization Benefiting Meta-Learning_20250918|Balancing Sparse RNNs with Hyperparameterization Benefiting Meta-Learning]] (77.5% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (77.1% similar)
- [[2025-09-18/Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations_20250918|Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations]] (76.6% similar)
- [[2025-09-19/Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior_20250919|Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior]] (76.1% similar)
- [[2025-09-22/Top-$k$ Feature Importance Ranking_20250922|Top-$k$ Feature Importance Ranking]] (76.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15429v1 Announce Type: new 
Abstract: Single-cell RNA-seq provides detailed molecular snapshots of individual cells but is notoriously noisy. Variability stems from biological differences, PCR amplification bias, limited sequencing depth, and low capture efficiency, making it challenging to adapt computational pipelines to heterogeneous datasets or evolving technologies. As a result, most studies still rely on principal component analysis (PCA) for dimensionality reduction, valued for its interpretability and robustness. Here, we improve upon PCA with a Random Matrix Theory (RMT)-based approach that guides the inference of sparse principal components using existing sparse PCA algorithms. We first introduce a novel biwhitening method, inspired by the Sinkhorn-Knopp algorithm, that simultaneously stabilizes variance across genes and cells. This enables the use of an RMT-based criterion to automatically select the sparsity level, rendering sparse PCA nearly parameter-free. Our mathematically grounded approach retains the interpretability of PCA while enabling robust, hands-off inference of sparse principal components. Across seven single-cell RNA-seq technologies and four sparse PCA algorithms, we show that this method systematically improves the reconstruction of the principal subspace and consistently outperforms PCA-, autoencoder-, and diffusion-based methods in cell-type classification tasks.

## 🔍 Abstract (한글 번역)

arXiv:2509.15429v1 발표 유형: 신규  
초록: 단일 세포 RNA-seq는 개별 세포의 상세한 분자적 스냅샷을 제공하지만, 소음이 많기로 악명 높습니다. 변동성은 생물학적 차이, PCR 증폭 편향, 제한된 시퀀싱 깊이 및 낮은 포획 효율성에서 비롯되며, 이로 인해 이질적인 데이터셋이나 진화하는 기술에 컴퓨팅 파이프라인을 적응시키는 것이 어렵습니다. 그 결과, 대부분의 연구는 여전히 해석 가능성과 견고함으로 인해 차원 축소를 위해 주성분 분석(PCA)에 의존하고 있습니다. 여기서 우리는 기존의 희소 PCA 알고리즘을 사용하여 희소 주성분의 추론을 안내하는 랜덤 행렬 이론(RMT) 기반 접근 방식을 통해 PCA를 개선합니다. 우리는 먼저 Sinkhorn-Knopp 알고리즘에서 영감을 받은 새로운 이중 백색화 방법을 소개하여 유전자와 세포 전반에 걸쳐 분산을 안정화합니다. 이를 통해 RMT 기반 기준을 사용하여 희소 수준을 자동으로 선택할 수 있게 하여, 희소 PCA를 거의 매개변수 없이 사용할 수 있게 합니다. 우리의 수학적으로 근거 있는 접근 방식은 PCA의 해석 가능성을 유지하면서 희소 주성분의 견고하고 자동화된 추론을 가능하게 합니다. 7개의 단일 세포 RNA-seq 기술과 4개의 희소 PCA 알고리즘 전반에 걸쳐, 이 방법이 주성분 부분 공간의 재구성을 체계적으로 개선하고 세포 유형 분류 작업에서 PCA-, 오토인코더-, 확산 기반 방법을 일관되게 능가함을 보여줍니다.

## 📝 요약

이 논문은 단일 세포 RNA 시퀀싱의 잡음 문제를 해결하기 위해 랜덤 행렬 이론(RMT)을 기반으로 한 새로운 방법론을 제안합니다. 기존의 희소 PCA 알고리즘을 활용하여 희소 주성분을 추론하는 데 도움을 주는 이 접근법은 Sinkhorn-Knopp 알고리즘에서 영감을 받은 새로운 이중 표백 방법을 도입하여 유전자와 세포 간의 분산을 안정화합니다. 이로 인해 자동으로 희소성을 선택할 수 있어 거의 매개변수 없이 희소 PCA를 수행할 수 있습니다. 제안된 방법은 7개의 단일 세포 RNA 시퀀싱 기술과 4개의 희소 PCA 알고리즘에 걸쳐 주성분 공간의 재구성을 개선하고, 세포 유형 분류 작업에서 기존의 PCA, 오토인코더, 확산 기반 방법보다 일관되게 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 단일 세포 RNA-seq 데이터의 잡음을 줄이기 위해 랜덤 행렬 이론(RMT)을 기반으로 한 희소 주성분 분석 방법을 제안합니다.

- 2. Sinkhorn-Knopp 알고리즘에서 영감을 받은 새로운 이중 백색화 방법을 도입하여 유전자와 세포 간의 분산을 안정화합니다.

- 3. RMT 기반 기준을 사용하여 희소성 수준을 자동으로 선택할 수 있어 희소 PCA를 거의 매개변수 없이 수행할 수 있습니다.

- 4. 제안된 방법은 7개의 단일 세포 RNA-seq 기술과 4개의 희소 PCA 알고리즘에서 주성분 공간 재구성을 개선하고, 세포 유형 분류 작업에서 기존 방법들을 능가합니다.

---

*Generated on 2025-09-22 15:14:07*