# Diffusion-Based Cross-Modal Feature Extraction for Multi-Label Classification

**Korean Title:** 다중 라벨 분류를 위한 확산 기반의 교차 모달 특징 추출

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Cross-modal Feature Extraction

## 🔗 유사한 논문
- [[2025-09-19/DiffCut_ Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut_20250919|DiffCut Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut]] (83.2% similar)
- [[2025-09-17/SpecDiff_ Accelerating Diffusion Model Inference with Self-Speculation_20250917|SpecDiff Accelerating Diffusion Model Inference with Self-Speculation]] (82.1% similar)
- [[2025-09-19/Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (81.3% similar)
- [[2025-09-19/MARIC_ Multi-Agent Reasoning for Image Classification_20250919|MARIC Multi-Agent Reasoning for Image Classification]] (80.3% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (80.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15553v1 Announce Type: cross 
Abstract: Multi-label classification has broad applications and depends on powerful representations capable of capturing multi-label interactions. We introduce \textit{Diff-Feat}, a simple but powerful framework that extracts intermediate features from pre-trained diffusion-Transformer models for images and text, and fuses them for downstream tasks. We observe that for vision tasks, the most discriminative intermediate feature along the diffusion process occurs at the middle step and is located in the middle block in Transformer. In contrast, for language tasks, the best feature occurs at the noise-free step and is located in the deepest block. In particular, we observe a striking phenomenon across varying datasets: a mysterious "Layer $12$" consistently yields the best performance on various downstream classification tasks for images (under DiT-XL/2-256$\times$256). We devise a heuristic local-search algorithm that pinpoints the locally optimal "image-text"$\times$"block-timestep" pair among a few candidates, avoiding an exhaustive grid search. A simple fusion-linear projection followed by addition-of the selected representations yields state-of-the-art performance: 98.6\% mAP on MS-COCO-enhanced and 45.7\% mAP on Visual Genome 500, surpassing strong CNN, graph, and Transformer baselines by a wide margin. t-SNE and clustering metrics further reveal that \textit{Diff-Feat} forms tighter semantic clusters than unimodal counterparts. The code is available at https://github.com/lt-0123/Diff-Feat.

## 🔍 Abstract (한글 번역)

arXiv:2509.15553v1 발표 유형: 교차  
초록: 다중 레이블 분류는 광범위한 응용 분야를 가지고 있으며, 다중 레이블 상호작용을 포착할 수 있는 강력한 표현에 의존합니다. 우리는 이미지와 텍스트에 대한 사전 학습된 확산-트랜스포머 모델에서 중간 특징을 추출하고, 이를 후속 작업에 융합하는 간단하지만 강력한 프레임워크인 \textit{Diff-Feat}를 소개합니다. 비전 작업의 경우, 확산 과정에서 가장 변별력 있는 중간 특징은 중간 단계에서 발생하며 트랜스포머의 중간 블록에 위치한다는 것을 관찰했습니다. 반면, 언어 작업의 경우, 최고의 특징은 잡음이 없는 단계에서 발생하며 가장 깊은 블록에 위치합니다. 특히, 다양한 데이터셋에서 놀라운 현상을 관찰했는데, 신비로운 "레이어 $12$"가 이미지에 대한 다양한 후속 분류 작업에서 일관되게 최고의 성능을 발휘합니다 (DiT-XL/2-256$\times$256 하에서). 우리는 몇 가지 후보 중에서 "이미지-텍스트"$\times$"블록-시간 단계" 쌍을 지역 최적화하는 휴리스틱 지역 탐색 알고리즘을 고안하여, 전체적인 그리드 탐색을 피합니다. 선택된 표현을 단순 융합-선형 투영 후 더하는 방식으로 최첨단 성능을 달성했습니다: MS-COCO-향상에서 98.6% mAP와 Visual Genome 500에서 45.7% mAP로, 강력한 CNN, 그래프, 트랜스포머 기준선을 크게 능가합니다. t-SNE 및 클러스터링 메트릭은 \textit{Diff-Feat}가 단일 모달 대안보다 더 긴밀한 의미적 클러스터를 형성한다는 것을 추가로 보여줍니다. 코드는 https://github.com/lt-0123/Diff-Feat에서 사용할 수 있습니다.

## 📝 요약

다중 레이블 분류에 효과적인 \textit{Diff-Feat} 프레임워크를 소개합니다. 이는 사전 학습된 확산-트랜스포머 모델에서 중간 특징을 추출하여 이미지와 텍스트의 다운스트림 작업에 활용합니다. 시각적 작업에서는 중간 단계의 중간 블록에서 가장 구별되는 특징이 나타나며, 언어 작업에서는 노이즈가 없는 단계의 가장 깊은 블록에서 최적의 특징이 발견됩니다. 특히 다양한 데이터셋에서 "Layer 12"가 이미지 분류 작업에서 일관되게 최고의 성능을 보였습니다. 우리는 지역 최적의 "이미지-텍스트"와 "블록-시간 단계" 쌍을 찾기 위한 휴리스틱 탐색 알고리즘을 개발했습니다. 선택된 표현의 단순한 융합-선형 투영과 추가는 MS-COCO-enhanced에서 98.6% mAP, Visual Genome 500에서 45.7% mAP를 기록하며 기존의 CNN, 그래프, 트랜스포머 기반 모델을 능가합니다. t-SNE 및 클러스터링 지표는 \textit{Diff-Feat}가 단일 모달보다 더 밀집된 의미론적 클러스터를 형성함을 보여줍니다.

## 🎯 주요 포인트

- 1. \textit{Diff-Feat}는 사전 학습된 확산-Transformer 모델에서 중간 특징을 추출하여 이미지와 텍스트의 멀티라벨 분류를 위한 강력한 표현을 제공하는 프레임워크입니다.

- 2. 시각적 작업에서는 중간 단계와 Transformer의 중간 블록에서 가장 구별력 있는 특징이 나타나며, 언어 작업에서는 잡음이 없는 단계와 가장 깊은 블록에서 최상의 특징이 나타납니다.

- 3. 다양한 데이터셋에서 "Layer 12"가 이미지 분류 작업에서 일관되게 최고의 성능을 발휘하는 현상이 관찰되었습니다.

- 4. 지역 최적의 "이미지-텍스트"와 "블록-타임스텝" 쌍을 찾기 위한 휴리스틱 로컬 탐색 알고리즘을 개발하여, 전체 그리드 탐색을 피했습니다.

- 5. 선택된 표현의 간단한 융합-선형 투영과 추가를 통해 MS-COCO-enhanced에서 98.6% mAP, Visual Genome 500에서 45.7% mAP를 기록하며, 기존의 강력한 CNN, 그래프, Transformer 기반을 크게 능가하는 성능을 보여줍니다.

---

*Generated on 2025-09-22 14:01:30*