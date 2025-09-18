
# MAP: End-to-End Autonomous Driving with Map-Assisted Planning

**Korean Title:** 지도 지원 계획을 활용한 엔드 투 엔드 자율 주행입니다.

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Semantic Map Features|Semantic Map Features]] [[keywords/broad/Autonomous Driving|Autonomous Driving]] [[keywords/broad/End-to-End Trajectory Planning|End-to-End Trajectory Planning]] [[keywords/specific/Online Mapping Module|Online Mapping Module]] [[keywords/unique/MAP (Map-Assisted Planning|MAP (Map-Assisted Planning]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Semantic Map Features
**🔬 Broad Technical**: Autonomous Driving, End-to-End Trajectory Planning
**🔗 Specific Connectable**: Online Mapping Module
**⭐ Unique Technical**: MAP (Map-Assisted Planning

**ArXiv ID**: [2509.13926](https://arxiv.org/abs/2509.13926)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2509.13926.pdf)


## 🏷️ 추출된 키워드



`Autonomous Driving` • 

`Trajectory Planning` • 

`Segmentation-based Map Features` • 

`MAP (Map-Assisted Planning` • 

`V2X Cooperation`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13926v1 Announce Type: cross 
Abstract: In recent years, end-to-end autonomous driving has attracted increasing attention for its ability to jointly model perception, prediction, and planning within a unified framework. However, most existing approaches underutilize the online mapping module, leaving its potential to enhance trajectory planning largely untapped. This paper proposes MAP (Map-Assisted Planning), a novel map-assisted end-to-end trajectory planning framework. MAP explicitly integrates segmentation-based map features and the current ego status through a Plan-enhancing Online Mapping module, an Ego-status-guided Planning module, and a Weight Adapter based on current ego status. Experiments conducted on the DAIR-V2X-seq-SPD dataset demonstrate that the proposed method achieves a 16.6% reduction in L2 displacement error, a 56.2% reduction in off-road rate, and a 44.5% improvement in overall score compared to the UniV2X baseline, even without post-processing. Furthermore, it achieves top ranking in Track 2 of the End-to-End Autonomous Driving through V2X Cooperation Challenge of MEIS Workshop @CVPR2025, outperforming the second-best model by 39.5% in terms of overall score. These results highlight the effectiveness of explicitly leveraging semantic map features in planning and suggest new directions for improving structure design in end-to-end autonomous driving systems. Our code is available at https://gitee.com/kymkym/map.git

## 🔍 Abstract (한글 번역)

arXiv:2509.13926v1 발표 유형: 교차
최근 몇 년간, end-to-end 자율 주행은 인식, 예측 및 계획을 통합된 프레임워크 내에서 함께 모델링할 수 있는 능력으로 인해 점점 더 많은 관심을 끌고 있습니다. 그러나 대부분의 기존 접근 방식은 온라인 매핑 모듈을 충분히 활용하지 않아 궤적 계획을 향상시킬 수 있는 잠재력을 대부분 활용하지 못하고 있습니다. 본 논문에서는 MAP (Map-Assisted Planning)이라는 새로운 맵 지원 end-to-end 궤적 계획 프레임워크를 제안합니다. MAP은 분할 기반 맵 특징과 현재 자이 상태를 명시적으로 통합하여 Plan-enhancing Online Mapping 모듈, Ego-status-guided Planning 모듈 및 현재 자이 상태에 기반한 Weight Adapter를 통해 구현됩니다. DAIR-V2X-seq-SPD 데이터셋에서 수행된 실험 결과, 제안된 방법은 후처리 없이도 UniV2X 기준에 비해 L2 변위 오차를 16.6% 줄이고, 산에서 벗어난 비율을 56.2% 줄이고, 전체 점수를 44.5% 향상시킵니다. 또한, MEIS Workshop @CVPR2025의 End-to-End 자율 주행을 통한 V2X 협력 도전의 Track 2에서 최고 순위를 차지하여, 전체 점수 측면에서 두 번째로 뛰어난 모델을 39.5% 능가합니다. 이러한 결과는 계획에서 의미 있는 맵 특징을 명시적으로 활용하는 효과를 강조하며, end-to-end 자율 주행 시스템의 구조 설계 개선을 위한 새로운 방향을 제안합니다. 우리의 코드는 https://gitee.com/kymkym/map.git에서 사용할 수 있습니다.

## 📝 요약

이 연구는 자율 주행 기술에서 온라인 맵 모듈을 활용하여 궤적 계획을 향상시키는 새로운 MAP (Map-Assisted Planning) 프레임워크를 제안한다. MAP은 세분화 기반 맵 특징과 현재 자아 상태를 명시적으로 통합하여 궤적 계획을 개선한다. DAIR-V2X-seq-SPD 데이터셋에서 실험한 결과, 제안된 방법은 L2 이동 에러를 16.6% 줄이고, 비도로 주행률을 56.2% 줄이며, 전체 점수를 44.5% 향상시켰다. 또한 MEIS Workshop @CVPR2025의 End-to-End Autonomous Driving through V2X Cooperation Challenge Track 2에서 최고 순위를 달성했다. 이러한 결과는 의미 있는 맵 특징을 계획에 명시적으로 활용하는 효과를 강조하며, 자율 주행 시스템의 구조 설계 개선을 위한 새로운 방향을 제안한다.

## 🎯 주요 포인트


- 1. MAP (Map-Assisted Planning)은 새로운 지도 지원형 엔드 투 엔드 궤적 계획 프레임워크를 제안한다.

- 2. 제안된 방법은 L2 이동 오차를 16.6% 감소시키고, 비도로 비율을 56.2% 줄이며, 전반적인 점수를 44.5% 향상시킨다.

- 3. MAP은 MEIS 워크샵 @CVPR2025의 End-to-End 자율 주행을 통한 V2X 협력 도전의 Track 2에서 최고 순위를 달성한다.


---

*Generated on 2025-09-18 16:23:46*