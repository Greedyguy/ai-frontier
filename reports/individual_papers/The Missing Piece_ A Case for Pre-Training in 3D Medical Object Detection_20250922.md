# The Missing Piece: A Case for Pre-Training in 3D Medical Object Detection

**Korean Title:** 누락된 조각: 3D 의료 객체 탐지에서 사전 훈련의 필요성에 대한 사례

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Reconstruction-based Pre-training|Reconstruction-based Pre-training]] [[keywords/specific/Self-supervised Pre-training|Self-supervised Pre-training]] [[keywords/specific/CNNs and Transformers|CNNs and Transformers]] [[keywords/broad/3D Medical Object Detection|3D Medical Object Detection]] [[keywords/broad/Computer Vision|Computer Vision]] [[categories/cs.LG|cs.LG]] [[2025-09-18/Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model_20250918|Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model]] (81.7% similar) [[2025-09-17/Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation_20250917|Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation]] (80.6% similar) [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Self-supervised Pre-training, Reconstruction-based Pre-training
**🔬 Broad Technical**: 3D Medical Object Detection, Computer Vision
## 🔗 유사한 논문
- [[2025-09-18/Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model_20250918|Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model]] (81.7% similar)
- [[2025-09-17/Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation_20250917|Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation]] (80.6% similar)
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (80.6% similar)
- [[2025-09-22/Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture_20250922|Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture]] (80.5% similar)
- [[2025-09-18/Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT_20250918|Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT]] (80.0% similar)


**ArXiv ID**: [2509.15947](https://arxiv.org/abs/2509.15947)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.15947.pdf)


**ArXiv ID**: [2509.15947](https://arxiv.org/abs/2509.15947)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.15947.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Volumetric Information Utilization
**🔗 Specific Connectable**: Self-supervised Pre-training, Reconstruction-based Pre-training
**🔬 Broad Technical**: 3D Medical Object Detection, Computer Vision

## 🏷️ 추출된 키워드



`3D Medical Object Detection` • 

`Computer Vision` • 

`Self-supervised Pre-training` • 

`Reconstruction-based Pre-training`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15947v1 Announce Type: cross 
Abstract: Large-scale pre-training holds the promise to advance 3D medical object detection, a crucial component of accurate computer-aided diagnosis. Yet, it remains underexplored compared to segmentation, where pre-training has already demonstrated significant benefits. Existing pre-training approaches for 3D object detection rely on 2D medical data or natural image pre-training, failing to fully leverage 3D volumetric information. In this work, we present the first systematic study of how existing pre-training methods can be integrated into state-of-the-art detection architectures, covering both CNNs and Transformers. Our results show that pre-training consistently improves detection performance across various tasks and datasets. Notably, reconstruction-based self-supervised pre-training outperforms supervised pre-training, while contrastive pre-training provides no clear benefit for 3D medical object detection. Our code is publicly available at: https://github.com/MIC-DKFZ/nnDetection-finetuning.

## 🔍 Abstract (한글 번역)

arXiv:2509.15947v1 발표 유형: 교차  
초록: 대규모 사전 학습은 정확한 컴퓨터 보조 진단의 중요한 구성 요소인 3D 의료 객체 탐지를 발전시킬 가능성을 가지고 있습니다. 그러나 사전 학습이 이미 상당한 이점을 보여준 세분화와 비교할 때, 3D 의료 객체 탐지에 대한 연구는 상대적으로 미흡합니다. 기존의 3D 객체 탐지를 위한 사전 학습 접근법은 2D 의료 데이터 또는 자연 이미지 사전 학습에 의존하여 3D 볼륨 정보를 충분히 활용하지 못하고 있습니다. 본 연구에서는 기존 사전 학습 방법을 최첨단 탐지 아키텍처에 통합하는 첫 번째 체계적인 연구를 제시하며, CNN과 트랜스포머를 모두 다룹니다. 우리의 결과는 사전 학습이 다양한 작업과 데이터셋에서 탐지 성능을 일관되게 향상시킨다는 것을 보여줍니다. 특히, 재구성 기반의 자가 지도 사전 학습이 지도 사전 학습보다 우수한 성능을 보이며, 대조적 사전 학습은 3D 의료 객체 탐지에 명확한 이점을 제공하지 못합니다. 우리의 코드는 다음에서 공개적으로 이용 가능합니다: https://github.com/MIC-DKFZ/nnDetection-finetuning.

## 📝 요약

이 논문은 3D 의료 객체 탐지 분야에서 대규모 사전 학습의 잠재력을 탐구합니다. 기존의 사전 학습 방법들이 2D 의료 데이터나 자연 이미지에 의존하여 3D 부피 정보를 충분히 활용하지 못하는 문제를 지적합니다. 연구진은 최신 탐지 아키텍처에 기존 사전 학습 방법을 통합하는 체계적인 연구를 수행하였으며, 그 결과 사전 학습이 다양한 작업과 데이터셋에서 탐지 성능을 일관되게 향상시킴을 발견했습니다. 특히, 재구성 기반의 자가 지도 사전 학습이 지도 학습을 능가하는 성능을 보였고, 대조 학습은 3D 의료 객체 탐지에 명확한 이점을 제공하지 못했습니다. 연구에 사용된 코드는 공개되어 있습니다.

## 🎯 주요 포인트


- 1. 대규모 사전 학습은 3D 의료 객체 탐지의 발전 가능성을 지니고 있으며, 이는 정확한 컴퓨터 보조 진단의 핵심 요소이다.

- 2. 기존의 3D 객체 탐지를 위한 사전 학습 방법은 2D 의료 데이터나 자연 이미지 사전 학습에 의존하여 3D 볼륨 정보를 충분히 활용하지 못하고 있다.

- 3. 본 연구는 CNN과 트랜스포머를 포함한 최신 탐지 아키텍처에 기존 사전 학습 방법을 통합하는 첫 체계적 연구를 제시한다.

- 4. 사전 학습은 다양한 작업과 데이터셋에서 탐지 성능을 일관되게 향상시키며, 재구성 기반의 자가 지도 사전 학습이 지도 사전 학습보다 우수한 성능을 보인다.

- 5. 대조적 사전 학습은 3D 의료 객체 탐지에 명확한 이점을 제공하지 않는다.


---

*Generated on 2025-09-22 15:44:42*