# Detail Across Scales: Multi-Scale Enhancement for Full Spectrum Neural Representations

**Korean Title:** 스케일 전반의 세부사항: 전체 스펙트럼 신경 표현을 위한 다중 스케일 향상

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-scale Neural Representation

## 🔗 유사한 논문
- [[2025-09-19/MaRVIn_ A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration_20250919|MaRVIn A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration]] (79.9% similar)
- [[2025-09-22/A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction_20250922|A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction]] (79.2% similar)
- [[2025-09-17/Data Denoising and Derivative Estimation for Data-Driven Modeling of Nonlinear Dynamical Systems_20250917|Data Denoising and Derivative Estimation for Data-Driven Modeling of Nonlinear Dynamical Systems]] (78.9% similar)
- [[2025-09-22/Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data_20250922|Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data]] (78.7% similar)
- [[2025-09-18/Task-Aware Image Signal Processor for Advanced Visual Perception_20250918|Task-Aware Image Signal Processor for Advanced Visual Perception]] (78.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15494v1 Announce Type: new 
Abstract: Implicit neural representations (INRs) have emerged as a compact and parametric alternative to discrete array-based data representations, encoding information directly in neural network weights to enable resolution-independent representation and memory efficiency. However, existing INR approaches, when constrained to compact network sizes, struggle to faithfully represent the multi-scale structures, high-frequency information, and fine textures that characterize the majority of scientific datasets. To address this limitation, we propose WIEN-INR, a wavelet-informed implicit neural representation that distributes modeling across different resolution scales and employs a specialized kernel network at the finest scale to recover subtle details. This multi-scale architecture allows for the use of smaller networks to retain the full spectrum of information while preserving the training efficiency and reducing storage cost. Through extensive experiments on diverse scientific datasets spanning different scales and structural complexities, WIEN-INR achieves superior reconstruction fidelity while maintaining a compact model size. These results demonstrate WIEN-INR as a practical neural representation framework for high-fidelity scientific data encoding, extending the applicability of INRs to domains where efficient preservation of fine detail is essential.

## 🔍 Abstract (한글 번역)

arXiv:2509.15494v1 발표 유형: 신규  
초록: 암묵적 신경 표현(INRs)은 불연속 배열 기반 데이터 표현의 압축적이고 매개변수적인 대안으로 부상하고 있으며, 신경망 가중치에 직접 정보를 인코딩하여 해상도 독립적인 표현과 메모리 효율성을 가능하게 합니다. 그러나 기존의 INR 접근 방식은 네트워크 크기를 압축적으로 제한할 경우, 대부분의 과학 데이터셋을 특징짓는 다중 스케일 구조, 고주파 정보 및 미세한 질감을 충실하게 표현하는 데 어려움을 겪습니다. 이러한 한계를 해결하기 위해, 우리는 WIEN-INR을 제안합니다. 이는 다양한 해상도 스케일에 걸쳐 모델링을 분배하고, 가장 세밀한 스케일에서 미세한 세부 사항을 복원하기 위해 특수화된 커널 네트워크를 사용하는 웨이블릿 정보 기반 암묵적 신경 표현입니다. 이 다중 스케일 아키텍처는 더 작은 네트워크를 사용하여 전체 정보 스펙트럼을 유지하면서도 학습 효율성을 보존하고 저장 비용을 줄일 수 있게 합니다. 다양한 스케일과 구조적 복잡성을 아우르는 다양한 과학 데이터셋에 대한 광범위한 실험을 통해, WIEN-INR은 압축된 모델 크기를 유지하면서도 우수한 재구성 충실도를 달성합니다. 이러한 결과는 WIEN-INR이 고충실도의 과학 데이터 인코딩을 위한 실용적인 신경 표현 프레임워크임을 입증하며, 세부 사항의 효율적인 보존이 필수적인 분야에서 INRs의 적용 가능성을 확장합니다.

## 📝 요약

WIEN-INR은 기존의 암시적 신경 표현(INR)이 작은 네트워크 크기에서 다중 스케일 구조와 고주파 정보를 제대로 표현하지 못하는 문제를 해결하기 위해 제안되었습니다. 이 방법은 웨이블릿 정보를 활용하여 다양한 해상도 스케일에서 모델링을 분배하고, 가장 세밀한 스케일에서는 특수한 커널 네트워크를 사용하여 미세한 세부 사항을 복원합니다. 이를 통해 작은 네트워크로도 전체 정보를 유지하면서 훈련 효율성과 저장 비용을 줄일 수 있습니다. 다양한 과학 데이터셋에 대한 실험 결과, WIEN-INR은 높은 재구성 충실도를 유지하면서도 모델 크기를 작게 유지하는 데 성공하였으며, 과학 데이터의 고충실도 인코딩에 실용적인 신경 표현 프레임워크로서의 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. 암묵적 신경 표현(INRs)은 해상도 독립적 표현과 메모리 효율성을 제공하는 데이터 표현 방식으로 부상하고 있다.

- 2. 기존 INR 접근 방식은 네트워크 크기가 작을 때 다중 스케일 구조와 고주파 정보를 충실히 표현하는 데 한계가 있다.

- 3. WIEN-INR은 웨이블릿 정보를 활용하여 다양한 해상도 스케일에 걸쳐 모델링을 분산하고, 세밀한 디테일을 복구하기 위한 특수 커널 네트워크를 사용한다.

- 4. WIEN-INR은 다양한 과학 데이터셋에서 높은 재구성 충실도를 유지하면서도 컴팩트한 모델 크기를 유지한다.

- 5. WIEN-INR은 세밀한 디테일의 효율적 보존이 필수적인 분야에 INRs의 적용 가능성을 확장하는 실용적인 신경 표현 프레임워크로 입증되었다.

---

*Generated on 2025-09-22 15:16:17*