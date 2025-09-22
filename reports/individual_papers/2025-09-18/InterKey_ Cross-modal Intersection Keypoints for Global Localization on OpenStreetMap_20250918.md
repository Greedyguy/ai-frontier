
# InterKey: Cross-modal Intersection Keypoints for Global Localization on OpenStreetMap

**Korean Title:** 인터키: 오픈스트리트맵에서의 글로벌 로컬라이제이션을 위한 교차 모달 교차점

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Robust Vehicle Localization

## 🔗 유사한 논문
- [[Semantic-Enhanced_Cross-Modal_Place_Recognition_for_Robust_Robot_Localization_20250918|Semantic-Enhanced Cross-Modal Place Recognition for Robust Robot Localization]] (80.6% similar)
- [[MAP: End-to-End Autonomous Driving with Map-Assisted Planning]] (79.8% similar)
- [[MOCHA: Multi-modal Objects-aware Cross-arcHitecture Alignment]] (78.4% similar)
- [[NavMoE_Hybrid_Model-_and_Learning-based_Traversability_Estimation_for_Local_Navigation_via_Mixture_of_Experts_20250918|NavMoE: Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts]] (78.1% similar)
- [[MCGS-SLAM_A_Multi-Camera_SLAM_Framework_Using_Gaussian_Splatting_for_High-Fidelity_Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (77.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13857v1 Announce Type: cross 
Abstract: Reliable global localization is critical for autonomous vehicles, especially in environments where GNSS is degraded or unavailable, such as urban canyons and tunnels. Although high-definition (HD) maps provide accurate priors, the cost of data collection, map construction, and maintenance limits scalability. OpenStreetMap (OSM) offers a free and globally available alternative, but its coarse abstraction poses challenges for matching with sensor data. We propose InterKey, a cross-modal framework that leverages road intersections as distinctive landmarks for global localization. Our method constructs compact binary descriptors by jointly encoding road and building imprints from point clouds and OSM. To bridge modality gaps, we introduce discrepancy mitigation, orientation determination, and area-equalized sampling strategies, enabling robust cross-modal matching. Experiments on the KITTI dataset demonstrate that InterKey achieves state-of-the-art accuracy, outperforming recent baselines by a large margin. The framework generalizes to sensors that can produce dense structural point clouds, offering a scalable and cost-effective solution for robust vehicle localization.

## 🔍 Abstract (한글 번역)

arXiv:2509.13857v1 발표 유형: 교차
요약: 신뢰할 수 있는 전역 위치 결정은 자율 주행 차량에게 중요한데, 특히 GNSS가 저하되거나 사용할 수 없는 환경에서는 더욱 중요합니다. 예를 들어, 도시 협곡이나 터널과 같은 환경에서입니다. 고해상도(HD) 지도는 정확한 사전 정보를 제공하지만, 데이터 수집, 지도 구축 및 유지 비용이 확장 가능성을 제한합니다. OpenStreetMap (OSM)은 무료로 전 세계적으로 이용 가능한 대안을 제공하지만, 그 정제된 추상화는 센서 데이터와 일치시키는 데 어려움을 겪습니다. 우리는 글로벌 위치 결정을 위해 도로 교차로를 독특한 랜드마크로 활용하는 교차 모달 프레임워크인 InterKey를 제안합니다. 우리의 방법은 포인트 클라우드와 OSM으로부터 도로와 건물 흔적을 공동으로 인코딩하여 간결한 이진 설명자를 구축합니다. 모달 간격을 줄이기 위해 불일치 완화, 방향 결정 및 면적 균등 샘플링 전략을 소개하여 견고한 교차 모달 일치를 가능하게 합니다. KITTI 데이터셋에서의 실험 결과는 InterKey가 최신 기준선을 크게 능가하는 최첨단 정확도를 달성한다는 것을 보여줍니다. 이 프레임워크는 밀도 있는 구조적 포인트 클라우드를 생성할 수 있는 센서에 일반화되어, 견고한 차량 위치 결정을 위한 확장 가능하고 비용 효율적인 솔루션을 제공합니다.

## 📝 요약

자율 주행 차량에서 신뢰할 수 있는 전역 위치 결정은 중요하다. 특히 도심이나 터널과 같이 GNSS가 약화되거나 사용 불가능한 환경에서는 더욱 중요하다. 고해상도 지도는 정확한 사전 정보를 제공하지만 데이터 수집, 지도 구축 및 유지 비용이 제한적이다. OpenStreetMap (OSM)은 무료로 제공되지만 그로 인한 도로와 건물의 추상화 정도가 센서 데이터와 매칭하는 데 어려움을 준다. 우리는 InterKey라는 교차 모달 프레임워크를 제안한다. 이 방법은 도로 교차로를 독특한 랜드마크로 활용하여 전역 위치 결정을 한다. 실험 결과, InterKey는 최신 기준선을 크게 능가하는 최신 정확도를 달성한다. 이 프레임워크는 밀도 높은 구조적 포인트 클라우드를 생성할 수 있는 센서에 대해 일반화되며, 강력한 차량 위치 결정을 위한 확장 가능하고 비용 효율적인 솔루션을 제공한다.

## 🎯 주요 포인트

- 자율 주행 차량을 위한 신뢰할 수 있는 글로벌 로컬라이제이션이 중요하다.

- 고해상도 지도는 정확한 사전 정보를 제공하지만 데이터 수집 및 유지 보수 비용이 제한적이다.

- InterKey는 도로 교차로를 특징적인 랜드마크로 활용하여 글로벌 로컬라이제이션을 제안한다.

---

*Generated on 2025-09-18 17:04:56*