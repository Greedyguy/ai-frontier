# CrackSCF: Lightweight Cascaded Fusion Network for Robust and Efficient Structural Crack Segmentation

**Korean Title:** 크랙SCF: 견고하고 효율적인 구조적 균열 분할을 위한 경량급 계단식 융합 네트워크

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Lightweight Cascaded Fusion

## 🔗 유사한 논문
- [[2025-09-19/DiffCut_ Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut_20250919|DiffCut Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut]] (79.3% similar)
- [[2025-09-22/CAGE_ Continuity-Aware edGE Network Unlocks Robust Floorplan Reconstruction_20250922|CAGE Continuity-Aware edGE Network Unlocks Robust Floorplan Reconstruction]] (78.8% similar)
- [[2025-09-18/Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT_20250918|Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT]] (78.3% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (78.3% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (78.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2408.12815v4 Announce Type: replace-cross 
Abstract: Accurately segmenting structural cracks at the pixel level remains a major hurdle, as existing methods fail to integrate local textures with pixel dependencies, often leading to fragmented and incomplete predictions. Moreover, their high parameter counts and substantial computational demands hinder practical deployment on resource-constrained edge devices. To address these challenges, we propose CrackSCF, a Lightweight Cascaded Fusion Crack Segmentation Network designed to achieve robust crack segmentation with exceptional computational efficiency. We design a lightweight convolutional block (LRDS) to replace all standard convolutions. This approach efficiently captures local patterns while operating with a minimal computational footprint. For a holistic perception of crack structures, a lightweight Long-range Dependency Extractor (LDE) captures global dependencies. These are then intelligently unified with local patterns by our Staircase Cascaded Fusion Module (SCFM), ensuring the final segmentation maps are both seamless in continuity and rich in fine-grained detail. To comprehensively evaluate our method, we created the challenging TUT benchmark dataset and evaluated it alongside five other public datasets. The experimental results show that the CrackSCF method consistently outperforms the existing methods, and it demonstrates greater robustness in dealing with complex background noise. On the TUT dataset, CrackSCF achieved 0.8382 on F1 score and 0.8473 on mIoU, and it only required 4.79M parameters.

## 🔍 Abstract (한글 번역)

arXiv:2408.12815v4 발표 유형: 교차 대체  
초록: 구조적 균열을 픽셀 수준에서 정확하게 분할하는 것은 여전히 주요 과제로 남아 있으며, 기존 방법들은 지역 텍스처와 픽셀 종속성을 통합하지 못해 종종 단편적이고 불완전한 예측을 초래합니다. 게다가, 높은 매개변수 수와 상당한 계산 요구 사항은 자원이 제한된 엣지 장치에서의 실질적인 배포를 방해합니다. 이러한 문제를 해결하기 위해, 우리는 뛰어난 계산 효율성을 갖춘 견고한 균열 분할을 달성하기 위해 설계된 경량 계단식 융합 균열 분할 네트워크인 CrackSCF를 제안합니다. 우리는 모든 표준 합성곱을 대체하기 위해 경량 합성곱 블록(LRDS)을 설계했습니다. 이 접근 방식은 최소한의 계산 자원으로 지역 패턴을 효율적으로 포착합니다. 균열 구조에 대한 전체적인 인식을 위해, 경량 장거리 종속성 추출기(LDE)는 전역 종속성을 포착합니다. 이러한 종속성은 지역 패턴과 지능적으로 결합되어, 우리의 계단식 융합 모듈(SCFM)을 통해 최종 분할 맵이 연속성이 매끄럽고 세밀한 디테일이 풍부하도록 보장합니다. 우리의 방법을 종합적으로 평가하기 위해, 우리는 도전적인 TUT 벤치마크 데이터셋을 생성하고 다섯 개의 다른 공개 데이터셋과 함께 평가했습니다. 실험 결과, CrackSCF 방법이 기존 방법보다 일관되게 우수한 성능을 보였으며, 복잡한 배경 소음을 처리하는 데 있어 더 큰 견고성을 입증했습니다. TUT 데이터셋에서 CrackSCF는 F1 점수 0.8382와 mIoU 0.8473을 달성했으며, 단지 4.79M의 매개변수만 필요했습니다.

## 📝 요약

CrackSCF는 경량화된 계단식 융합 균열 분할 네트워크로, 구조적 균열을 픽셀 수준에서 정확하게 분할하는 데 중점을 둡니다. 기존 방법들은 지역 텍스처와 픽셀 의존성을 통합하지 못해 예측이 단편적이고 불완전한 경우가 많았습니다. CrackSCF는 경량의 컨볼루션 블록(LRDS)과 장거리 의존성 추출기(LDE)를 사용하여 지역 패턴과 전역 의존성을 효율적으로 포착하고, 이를 계단식 융합 모듈(SCFM)로 통합하여 연속적이고 세밀한 분할 지도를 생성합니다. TUT 벤치마크 데이터셋과 다섯 개의 공개 데이터셋에서 실험한 결과, CrackSCF는 기존 방법보다 뛰어난 성능을 보였으며, 복잡한 배경 소음에서도 높은 견고성을 입증했습니다. TUT 데이터셋에서 F1 점수 0.8382, mIoU 0.8473을 기록하며, 4.79M의 파라미터만을 필요로 했습니다.

## 🎯 주요 포인트

- 1. CrackSCF는 경량화된 계단식 융합 균열 분할 네트워크로, 구조적 균열을 효율적으로 분할하며 계산 효율성을 극대화합니다.

- 2. LRDS 경량화 컨볼루션 블록을 도입하여 지역 패턴을 최소한의 계산 자원으로 효과적으로 포착합니다.

- 3. LDE 경량화 장거리 의존성 추출기를 통해 전역 의존성을 포착하고, 이를 SCFM 모듈로 지역 패턴과 통합하여 연속적이고 세밀한 분할 지도를 생성합니다.

- 4. TUT 벤치마크 데이터셋을 포함한 다양한 데이터셋에서 CrackSCF는 기존 방법보다 우수한 성능을 보였으며, 복잡한 배경 노이즈에도 강한 내구성을 입증했습니다.

- 5. CrackSCF는 TUT 데이터셋에서 F1 점수 0.8382, mIoU 0.8473을 기록하며, 4.79M 파라미터만을 필요로 합니다.

---

*Generated on 2025-09-22 14:37:48*