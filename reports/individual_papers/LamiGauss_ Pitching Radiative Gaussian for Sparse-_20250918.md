
# LamiGauss: Pitching Radiative Gaussian for Sparse-View X-ray Laminography Reconstruction

**Korean Title:** LamiGauss: 희소 뷰 X-선 라미노그래피 재구성을 위한 방사 광선 가우시안 추정

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Sparse Projections Optimization|Sparse Projections Optimization]] [[keywords/broad/X-ray Computed Laminography|X-ray Computed Laminography]] [[keywords/broad/Sparse-view Reconstruction|Sparse-view Reconstruction]] [[keywords/specific/Gaussian Splatting|Gaussian Splatting]] [[keywords/unique/LamiGauss|LamiGauss]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Sparse Projections Optimization
**🔬 Broad Technical**: X-ray Computed Laminography, Sparse-view Reconstruction
**🔗 Specific Connectable**: Gaussian Splatting
**⭐ Unique Technical**: LamiGauss

**ArXiv ID**: [2509.13863](https://arxiv.org/abs/2509.13863)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13863.pdf)


## 🏷️ 추출된 키워드



`X-ray Computed Laminography` • 

`Sparse-view Reconstruction` • 

`Gaussian Splatting` • 

`LamiGauss` • 

`Sparse Projections Optimization`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13863v1 Announce Type: cross 
Abstract: X-ray Computed Laminography (CL) is essential for non-destructive inspection of plate-like structures in applications such as microchips and composite battery materials, where traditional computed tomography (CT) struggles due to geometric constraints. However, reconstructing high-quality volumes from laminographic projections remains challenging, particularly under highly sparse-view acquisition conditions. In this paper, we propose a reconstruction algorithm, namely LamiGauss, that combines Gaussian Splatting radiative rasterization with a dedicated detector-to-world transformation model incorporating the laminographic tilt angle. LamiGauss leverages an initialization strategy that explicitly filters out common laminographic artifacts from the preliminary reconstruction, preventing redundant Gaussians from being allocated to false structures and thereby concentrating model capacity on representing the genuine object. Our approach effectively optimizes directly from sparse projections, enabling accurate and efficient reconstruction with limited data. Extensive experiments on both synthetic and real datasets demonstrate the effectiveness and superiority of the proposed method over existing techniques. LamiGauss uses only 3$\%$ of full views to achieve superior performance over the iterative method optimized on a full dataset.

## 🔍 Abstract (한글 번역)

arXiv:2509.13863v1 발표 유형: 교차
요약: X선 컴퓨터 라미노그래피(CL)는 마이크로칩 및 복합 배터리 소재와 같은 플레이트 형태의 구조물의 비파괴 검사에 필수적이며, 기하학적 제약으로 인해 전통적인 컴퓨터 단층촬영(CT)가 어려워지는 경우에 사용됩니다. 그러나 라미노그래피 투사로부터 고품질 볼륨을 재구성하는 것은 여전히 어려운 과제입니다, 특히 매우 희소한 뷰 획득 조건 하에서. 본 논문에서는 가우시안 스플래팅 방사형 래스터화를 결합한 재구성 알고리즘인 LamiGauss를 제안합니다. 이 알고리즘은 라미노그래피 기울기 각도를 포함하는 전용 검출기-월드 변환 모델을 통합합니다. LamiGauss는 초기화 전략을 활용하여 초기 재구성으로부터 일반적인 라미노그래피 아티팩트를 명시적으로 필터링하여 가짜 구조에 재할당되는 중복 가우시안을 방지하고, 따라서 모델 용량을 진짜 객체를 표현하는 데 집중시킵니다. 우리의 접근 방식은 희소 투사로부터 직접 최적화를 효과적으로 수행하여, 제한된 데이터로 정확하고 효율적인 재구성을 가능하게 합니다. 합성 및 실제 데이터셋에 대한 광범위한 실험은 제안된 방법의 효과성과 우수성을 보여줍니다. LamiGauss는 전체 뷰의 3%만 사용하여 전체 데이터셋에 최적화된 반복적 방법보다 우수한 성능을 달성합니다.

## 📝 요약

이 연구는 X-선 계층 촬영 기술인 LamiGauss를 제안하고, 희소한 뷰 환경에서도 고품질의 볼륨 재구성을 가능하게 합니다. 이 알고리즘은 가우시안 스플래팅 방법과 램노그래픽 기울기 각도를 고려한 전용 감지기-세계 변환 모델을 결합하여 효율적인 재구성을 실현합니다. LamiGauss는 초기화 전략을 통해 램노그래픽 아티팩트를 명시적으로 필터링하고, 가짜 구조물에 잘못된 가우시안을 할당하지 않아 진짜 객체를 잘 표현할 수 있도록 모델 용량을 집중시킵니다. 실험 결과는 제안된 방법이 기존 기술보다 효과적이고 우수함을 입증하며, 전체 데이터셋에 최적화된 반복적 방법보다 3%의 뷰만 사용하여 우수한 성능을 달성합니다.

## 🎯 주요 포인트


- 1. X-선 계산 층상 촬영은 기하적 제약으로 전통적인 CT가 어려운 마이크로칩 및 복합 배터리 소재와 같은 판 모양 구조물의 비파괴 검사에 필수적이다.

- 2. LamiGauss는 가우시안 스플래팅 방사 래스터화와 층상 기울기 각도를 포함한 전용 감지기-세계 변환 모델을 결합한 재구성 알고리즘을 제안한다.

- 3. LamiGauss는 희소한 프로젝션에서 직접 최적화하여 제한된 데이터로 정확하고 효율적인 재구성을 가능하게 한다.


---

*Generated on 2025-09-18 16:44:20*