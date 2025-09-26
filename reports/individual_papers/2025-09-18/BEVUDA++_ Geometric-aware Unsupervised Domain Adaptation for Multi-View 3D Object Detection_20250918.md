---
keywords:
  - Uncertainty Quantification
  - Transfer Learning
  - Bird's Eye View perception
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.14151
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:38:38.124070",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Uncertainty Quantification",
    "Transfer Learning",
    "Bird's Eye View perception"
  ],
  "rejected_keywords": [
    "Geometric-aware teacher-student framework"
  ],
  "similarity_scores": {
    "Uncertainty Quantification": 0.8,
    "Transfer Learning": 0.78,
    "Bird's Eye View perception": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# BEVUDA++: Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection

**Korean Title:** BEVUDA++: 다중 뷰 3D 객체 감지를 위한 기하학 인식 무지도 도메인 적응

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Uncertainty Quantification|Uncertainty-guided Exponential Moving Average]], [[keywords/Transfer Learning|Domain Adaptation]]
**⚡ Unique Technical**: [[keywords/Bird's Eye View perception|Bird's Eye View perception]]

## 🔗 유사한 논문
- [[FishBEV_Distortion-Resilient_Bird's_Eye_View_Segmentation_with_Surround-View_Fisheye_Cameras_20250918|FishBEV: Distortion-Resilient Bird's Eye View Segmentation with Surround-View Fisheye Cameras]] (84.7% similar)
- [[GeoAware-VLA_Implicit_Geometry_Aware_Vision-Language-Action_Model_20250918|GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model]] (81.0% similar)
- [[Masked_Feature_Modeling_Enhances_Adaptive_Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (79.6% similar)
- [[MAP: End-to-End Autonomous Driving with Map-Assisted Planning]] (79.6% similar)
- [[VSE-MOT_Multi-Object_Tracking_in_Low-Quality_Video_Scenes_Guided_by_Visual_Semantic_Enhancement_20250918|VSE-MOT: Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (79.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14151v1 Announce Type: new 
Abstract: Vision-centric Bird's Eye View (BEV) perception holds considerable promise for autonomous driving. Recent studies have prioritized efficiency or accuracy enhancements, yet the issue of domain shift has been overlooked, leading to substantial performance degradation upon transfer. We identify major domain gaps in real-world cross-domain scenarios and initiate the first effort to address the Domain Adaptation (DA) challenge in multi-view 3D object detection for BEV perception. Given the complexity of BEV perception approaches with their multiple components, domain shift accumulation across multi-geometric spaces (e.g., 2D, 3D Voxel, BEV) poses a significant challenge for BEV domain adaptation. In this paper, we introduce an innovative geometric-aware teacher-student framework, BEVUDA++, to diminish this issue, comprising a Reliable Depth Teacher (RDT) and a Geometric Consistent Student (GCS) model. Specifically, RDT effectively blends target LiDAR with dependable depth predictions to generate depth-aware information based on uncertainty estimation, enhancing the extraction of Voxel and BEV features that are essential for understanding the target domain. To collaboratively reduce the domain shift, GCS maps features from multiple spaces into a unified geometric embedding space, thereby narrowing the gap in data distribution between the two domains. Additionally, we introduce a novel Uncertainty-guided Exponential Moving Average (UEMA) to further reduce error accumulation due to domain shifts informed by previously obtained uncertainty guidance. To demonstrate the superiority of our proposed method, we execute comprehensive experiments in four cross-domain scenarios, securing state-of-the-art performance in BEV 3D object detection tasks, e.g., 12.9\% NDS and 9.5\% mAP enhancement on Day-Night adaptation.

## 🔍 Abstract (한글 번역)

arXiv:2509.14151v1 발표 유형: 새로운
요약: 비전 중심적인 새 시점(BEV) 인식은 자율 주행에 상당한 잠재력을 가지고 있습니다. 최근 연구들은 효율성 또는 정확도 향상을 우선시했지만, 도메인 이동 문제는 간과되어 왔으며, 결과적으로 전송 시 중요한 성능 저하가 발생했습니다. 우리는 실제 세계의 교차 도메인 시나리오에서 주요 도메인 간격을 식별하고, BEV 인식을 위한 다중 뷰 3D 객체 감지의 도메인 적응(DA) 도전에 대한 최초의 노력을 시작합니다. 다중 기하학적 공간(예: 2D, 3D 복셀, BEV)을 횡단하는 BEV 인식 접근 방식의 복잡성을 감안할 때, 다중 기하학적 공간에서 도메인 이동 누적은 BEV 도메인 적응에 중요한 도전을 제기합니다. 본 논문에서는 이 문제를 줄이기 위해 신뢰할 수 있는 깊이 교사(RDT)와 기하학적 일관성 있는 학생(GCS) 모델로 이루어진 혁신적인 기하학적 인식 교사-학생 프레임워크인 BEVUDA++를 소개합니다. 특히, RDT는 신뢰할 수 있는 깊이 예측과 결합하여 불확실성 추정에 기반한 깊이 인식 정보를 생성하여, 목표 도메인을 이해하는 데 중요한 복셀 및 BEV 특징의 추출을 향상시킵니다. 도메인 이동을 협력적으로 줄이기 위해, GCS는 여러 공간의 특징을 통합된 기하학적 임베딩 공간으로 매핑하여 두 도메인 간 데이터 분포의 간격을 좁힙니다. 또한, 이전에 얻은 불확실성 안내에 의해 도메인 이동으로 인한 오류 누적을 더 줄이기 위해 새로운 불확실성 안내 지수 이동 평균(UEMA)를 소개합니다. 우리의 제안된 방법의 우수성을 증명하기 위해, 우리는 네 가지 교차 도메인 시나리오에서 포괄적인 실험을 수행하여, BEV 3D 객체 감지 작업에서 최첨단 성능을 확보하였으며, 예를 들어, Day-Night 적응에서 12.9\% NDS 및 9.5\% mAP 향상을 달성하였습니다.

## 📝 요약

자율 주행을 위한 시각 중심적 Bird's Eye View(BEV) 지각은 매우 유망하다. 그러나 최근 연구들은 효율성이나 정확성 향상을 우선시키면서 도메인 이동 문제를 간과해 왔다. 본 논문에서는 실제 세계의 다양한 도메인 시나리오에서 주요 도메인 갭을 식별하고 BEV 지각을 위한 다중 뷰 3D 객체 감지의 도메인 적응(DA) 도전에 대한 최초의 노력을 시작한다. 우리는 BEVUDA++라는 혁신적인 기하학적인 교사-학생 프레임워크를 소개하여 BEV 도메인 적응에 대한 이 문제를 줄이는데 기여한다. 이를 통해 우리는 BEV 3D 객체 감지 작업에서 최첨단 성능을 확보하며, Day-Night 적응에서 12.9% NDS 및 9.5% mAP 향상을 달성한다.

## 🎯 주요 포인트

- 1. 자율 주행을 위한 시각 중심적 Bird's Eye View (BEV) 인식에서 Domain Adaptation (DA) 도전에 대한 첫 번째 노력을 시작함

- 2. BEVUDA++는 Reliable Depth Teacher (RDT) 및 Geometric Consistent Student (GCS) 모델을 포함한 혁신적인 기하학 인식 선생님-학생 프레임워크를 소개

- 3. GCS는 여러 공간의 특징을 통합된 기하 임베딩 공간으로 매핑하여 두 도메인 간의 데이터 분포 차이를 줄이는 동시에 도메인 이동에 의한 오류 누적을 줄이는 데 기여함.

---

*Generated on 2025-09-18 17:04:27*