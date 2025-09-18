
# Benchmarking Dimensionality Reduction Techniques for Spatial Transcriptomics

**Korean Title:** 공간 전사체학을 위한 차원 축소 기술의 벤치마킹

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Pareto optimal analysis|Pareto optimal analysis]] [[keywords/broad/Dimensionality Reduction|Dimensionality Reduction]] [[keywords/broad/Spatial Transcriptomics|Spatial Transcriptomics]] [[keywords/specific/Cholangiocarcinoma|Cholangiocarcinoma]] [[keywords/unique/Cluster Marker Coherence (CMC|Cluster Marker Coherence (CMC]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Pareto optimal analysis
**🔬 Broad Technical**: Dimensionality Reduction, Spatial Transcriptomics
**🔗 Specific Connectable**: Cholangiocarcinoma
**⭐ Unique Technical**: Cluster Marker Coherence (CMC

**ArXiv ID**: [2509.13344](https://arxiv.org/abs/2509.13344)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13344.pdf)


## 🏷️ 추출된 키워드



`Dimensionality Reduction` • 

`Spatial Transcriptomics` • 

`Cholangiocarcinoma` • 

`Cluster Marker Coherence (CMC` • 

`Pareto optimal analysis`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13344v1 Announce Type: cross 
Abstract: We introduce a unified framework for evaluating dimensionality reduction techniques in spatial transcriptomics beyond standard PCA approaches. We benchmark six methods PCA, NMF, autoencoder, VAE, and two hybrid embeddings on a cholangiocarcinoma Xenium dataset, systematically varying latent dimensions ($k$=5-40) and clustering resolutions ($\rho$=0.1-1.2). Each configuration is evaluated using complementary metrics including reconstruction error, explained variance, cluster cohesion, and two novel biologically-motivated measures: Cluster Marker Coherence (CMC) and Marker Exclusion Rate (MER). Our results demonstrate distinct performance profiles: PCA provides a fast baseline, NMF maximizes marker enrichment, VAE balances reconstruction and interpretability, while autoencoders occupy a middle ground. We provide systematic hyperparameter selection using Pareto optimal analysis and demonstrate how MER-guided reassignment improves biological fidelity across all methods, with CMC scores improving by up to 12\% on average. This framework enables principled selection of dimensionality reduction methods tailored to specific spatial transcriptomics analyses.

## 🔍 Abstract (한글 번역)

arXiv:2509.13344v1 발표 유형: 교차
요약: 우리는 표준 PCA 접근법을 넘어 공간 전사체학에서 차원 축소 기술을 평가하기 위한 통합된 프레임워크를 소개합니다. 우리는 담낭암 Xenium 데이터셋에서 PCA, NMF, 오토인코더, VAE, 그리고 두 하이브리드 임베딩 방법을 벤치마킹하였으며, 잠재 차원 ($k$=5-40)과 클러스터링 해상도 ($\rho$=0.1-1.2)를 체계적으로 변화시켰습니다. 각 구성은 재구성 오차, 설명된 분산, 클러스터 응집력, 그리고 두 가지 새로운 생물학적 동기부여 지표인 클러스터 마커 일관성 (CMC) 및 마커 제외율 (MER)을 포함한 보완적인 메트릭을 사용하여 평가되었습니다. 우리의 결과는 명확한 성능 프로필을 보여줍니다: PCA는 빠른 기준을 제공하며, NMF는 마커 풍부성을 극대화시키고, VAE는 재구성과 해석가능성을 균형있게 유지하며, 오토인코더는 중간 지점을 차지합니다. 우리는 파레토 최적 분석을 사용하여 체계적인 하이퍼파라미터 선택을 제공하고, MER에 따른 재할당이 모든 방법에서 생물학적 충실성을 향상시키는 방법을 보여주며, CMC 점수가 평균적으로 12%까지 향상되는 것을 보여줍니다. 이 프레임워크는 특정 공간 전사체학 분석에 맞게 조정된 차원 축소 방법의 원칙적인 선택을 가능하게 합니다.

## 📝 요약

이 연구는 표준 PCA 접근법을 넘어 공간 전사체학에서 차원 축소 기술을 평가하기 위한 통합된 프레임워크를 소개한다. 이 연구에서는 cholangiocarcinoma Xenium 데이터셋을 사용하여 PCA, NMF, autoencoder, VAE, 및 두 하이브리드 임베딩 방법을 비교하였다. 잠재 차원($k$=5-40)과 클러스터링 해상도($\rho$=0.1-1.2)를 체계적으로 변화시키면서 각 구성은 재구성 오차, 설명된 분산, 클러스터 응집력, 그리고 두 가지 새로운 생물학적 측정치인 Cluster Marker Coherence (CMC)와 Marker Exclusion Rate (MER)를 사용하여 평가되었다. 결과는 PCA가 빠른 기준선을 제공하고, NMF가 마커 풍부성을 극대화하며, VAE가 재구성과 해석가능성을 균형있게 유지하는 것을 보여주었다. autoencoder는 중간 지점을 차지한다. Pareto 최적 분석을 사용하여 체계적인 하이퍼파라미터 선택을 제공하고, MER에 따른 재할당이 모든 방법에서 생물학적 충실성을 향상시키는 것을 보여주었다. 이 프레임워크는 특정 공간 전사체학 분석에 맞춘 차원 축소 방법의 원칙적인 선택을 가능하게 한다.

## 🎯 주요 포인트


- 1. 공간 전사체학에서 PCA, NMF, autoencoder, VAE 및 두 하이브리드 임베딩 방법을 벤치마킹하여 각각의 성능 프로필을 확인함.

- 2. 새로운 생물학적으로 동기부여된 측정 항목을 사용하여 각 구성을 평가하고 MER을 활용한 재할당이 생물학적 신뢰도 향상에 도움이 됨.

- 3. Pareto 최적 분석을 통해 체계적인 하이퍼파라미터 선택을 제공하고, CMC 점수가 평균 12% 향상되는 것을 보여줌.


---

*Generated on 2025-09-18 16:41:15*