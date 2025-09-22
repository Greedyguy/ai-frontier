# CAGE: Continuity-Aware edGE Network Unlocks Robust Floorplan Reconstruction

**Korean Title:** CAGE: 연속성 인식 에지 네트워크를 통한 견고한 평면도 재구성 구현

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Edge-Centric Formulation

## 🔗 유사한 논문
- [[2025-09-19/Multi-CAP_ A Multi-Robot Connectivity-Aware Hierarchical Coverage Path Planning Algorithm for Unknown Environments_20250919|Multi-CAP A Multi-Robot Connectivity-Aware Hierarchical Coverage Path Planning Algorithm for Unknown Environments]] (79.1% similar)
- [[2025-09-18/Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods Reviving Transformer for Graph Clustering]] (79.0% similar)
- [[2025-09-22/Causal Reasoning Elicits Controllable 3D Scene Generation_20250922|Causal Reasoning Elicits Controllable 3D Scene Generation]] (78.5% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (78.4% similar)
- [[2025-09-22/GenCAD-3D_ CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing_20250922|GenCAD-3D CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing]] (78.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15459v1 Announce Type: cross 
Abstract: We present \textbf{CAGE} (\textit{Continuity-Aware edGE}) network, a \textcolor{red}{robust} framework for reconstructing vector floorplans directly from point-cloud density maps. Traditional corner-based polygon representations are highly sensitive to noise and incomplete observations, often resulting in fragmented or implausible layouts. Recent line grouping methods leverage structural cues to improve robustness but still struggle to recover fine geometric details. To address these limitations, we propose a \textit{native} edge-centric formulation, modeling each wall segment as a directed, geometrically continuous edge. This representation enables inference of coherent floorplan structures, ensuring watertight, topologically valid room boundaries while improving robustness and reducing artifacts. Towards this design, we develop a dual-query transformer decoder that integrates perturbed and latent queries within a denoising framework, which not only stabilizes optimization but also accelerates convergence. Extensive experiments on Structured3D and SceneCAD show that \textbf{CAGE} achieves state-of-the-art performance, with F1 scores of 99.1\% (rooms), 91.7\% (corners), and 89.3\% (angles). The method also demonstrates strong cross-dataset generalization, underscoring the efficacy of our architectural innovations. Code and pretrained models will be released upon acceptance.

## 🔍 Abstract (한글 번역)

arXiv:2509.15459v1 발표 유형: 교차  
초록: 우리는 점 구름 밀도 지도에서 벡터 평면도를 직접 재구성하기 위한 \textbf{CAGE} (\textit{Continuity-Aware edGE}) 네트워크라는 \textcolor{red}{견고한} 프레임워크를 제시합니다. 전통적인 코너 기반 다각형 표현은 잡음과 불완전한 관측에 매우 민감하여 종종 단편적이거나 비현실적인 레이아웃을 초래합니다. 최근의 선 그룹화 방법은 구조적 단서를 활용하여 견고성을 향상시키지만 여전히 세밀한 기하학적 세부 사항을 복구하는 데 어려움을 겪습니다. 이러한 한계를 해결하기 위해, 우리는 각 벽 세그먼트를 지향적이고 기하학적으로 연속적인 엣지로 모델링하는 \textit{고유} 엣지 중심의 공식화를 제안합니다. 이 표현은 일관된 평면도 구조의 추론을 가능하게 하여, 견고성을 향상시키고 아티팩트를 줄이면서 밀폐되고 위상적으로 유효한 방 경계를 보장합니다. 이러한 설계를 위해, 우리는 교란된 쿼리와 잠재 쿼리를 통합하는 이중 쿼리 변환기 디코더를 개발하여, 최적화를 안정화할 뿐만 아니라 수렴 속도를 가속화합니다. Structured3D와 SceneCAD에 대한 광범위한 실험에서 \textbf{CAGE}는 99.1\% (방), 91.7\% (코너), 89.3\% (각도)의 F1 점수로 최첨단 성능을 달성합니다. 이 방법은 또한 강력한 데이터셋 간 일반화를 보여주며, 우리의 건축적 혁신의 효능을 강조합니다. 코드와 사전 학습된 모델은 승인 후 공개될 예정입니다.

## 📝 요약

CAGE 네트워크는 점 구름 밀도 지도에서 벡터 평면도를 직접 재구성하는 강력한 프레임워크입니다. 기존의 코너 기반 다각형 표현은 노이즈와 불완전한 관측에 민감하여 단편적이거나 비현실적인 레이아웃을 초래할 수 있습니다. 이를 해결하기 위해 CAGE는 각 벽면을 지향적이고 기하학적으로 연속적인 엣지로 모델링하는 엣지 중심의 새로운 접근 방식을 제안합니다. 이 방법은 일관된 평면도 구조를 추론하여 방의 경계가 밀폐되고 위상적으로 유효하도록 보장하며, 강건성을 향상시키고 아티팩트를 줄입니다. 또한, 이 설계를 위해 이중 쿼리 트랜스포머 디코더를 개발하여 최적화를 안정화하고 수렴을 가속화합니다. Structured3D와 SceneCAD 데이터셋에서의 실험 결과, CAGE는 방, 코너, 각도에서 각각 99.1%, 91.7%, 89.3%의 F1 점수를 기록하며 최첨단 성능을 달성했습니다. 이 방법은 데이터셋 간 일반화 능력도 뛰어나며, 코드와 사전 학습된 모델은 승인 후 공개될 예정입니다.

## 🎯 주요 포인트

- 1. CAGE 네트워크는 포인트 클라우드 밀도 맵으로부터 벡터 평면도를 재구성하는 강력한 프레임워크입니다.

- 2. 전통적인 코너 기반 다각형 표현은 노이즈와 불완전한 관측에 민감하여 단편적이거나 비현실적인 레이아웃을 초래할 수 있습니다.

- 3. CAGE는 각 벽 세그먼트를 지향적이고 기하학적으로 연속적인 엣지로 모델링하여 일관된 평면도 구조를 추론합니다.

- 4. 듀얼 쿼리 트랜스포머 디코더를 개발하여 최적화를 안정화하고 수렴 속도를 가속화합니다.

- 5. Structured3D와 SceneCAD에서 CAGE는 최첨단 성능을 달성하며, 데이터셋 간 강력한 일반화 능력을 보여줍니다.

---

*Generated on 2025-09-22 13:58:05*