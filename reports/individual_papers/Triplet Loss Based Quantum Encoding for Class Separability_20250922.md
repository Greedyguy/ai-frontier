# Triplet Loss Based Quantum Encoding for Class Separability

**Korean Title:** 트리플렛 손실 기반 양자 인코딩을 통한 클래스 분리 가능성

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Variational Quantum Classifier, Triplet Loss Function

## 🔗 유사한 논문
- [[2025-09-19/Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (81.4% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (79.7% similar)
- [[2025-09-17/Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures_20250917|Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures]] (79.7% similar)
- [[2025-09-22/Saccadic Vision for Fine-Grained Visual Classification_20250922|Saccadic Vision for Fine-Grained Visual Classification]] (79.6% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (79.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15705v1 Announce Type: cross 
Abstract: An efficient and data-driven encoding scheme is proposed to enhance the performance of variational quantum classifiers. This encoding is specially designed for complex datasets like images and seeks to help the classification task by producing input states that form well-separated clusters in the Hilbert space according to their classification labels. The encoding circuit is trained using a triplet loss function inspired by classical facial recognition algorithms, and class separability is measured via average trace distances between the encoded density matrices. Benchmark tests performed on various binary classification tasks on MNIST and MedMNIST datasets demonstrate considerable improvement over amplitude encoding with the same VQC structure while requiring a much lower circuit depth.

## 🔍 Abstract (한글 번역)

arXiv:2509.15705v1 발표 유형: 교차  
초록: 변분 양자 분류기의 성능을 향상시키기 위해 효율적이고 데이터 기반의 인코딩 방식이 제안됩니다. 이 인코딩은 이미지와 같은 복잡한 데이터셋에 특화되어 있으며, 분류 레이블에 따라 힐베르트 공간에서 잘 분리된 클러스터를 형성하는 입력 상태를 생성함으로써 분류 작업을 돕고자 합니다. 인코딩 회로는 고전적인 얼굴 인식 알고리즘에서 영감을 받은 트리플렛 손실 함수를 사용하여 훈련되며, 클래스 분리 가능성은 인코딩된 밀도 행렬 간의 평균 추적 거리로 측정됩니다. MNIST 및 MedMNIST 데이터셋에서 다양한 이진 분류 작업에 대해 수행된 벤치마크 테스트는 동일한 VQC 구조를 사용한 진폭 인코딩에 비해 상당한 개선을 보여주며, 훨씬 낮은 회로 깊이를 요구합니다.

## 📝 요약

이 논문은 복잡한 데이터셋의 분류 성능을 향상시키기 위해 변분 양자 분류기(VQC)에 효율적이고 데이터 기반의 인코딩 방식을 제안합니다. 이 인코딩은 이미지와 같은 복잡한 데이터셋에 적합하며, 힐베르트 공간에서 분류 라벨에 따라 잘 분리된 클러스터를 형성하는 입력 상태를 생성합니다. 인코딩 회로는 얼굴 인식 알고리즘에서 영감을 받은 트리플렛 손실 함수를 사용하여 훈련되며, 클래스 분리 가능성은 인코딩된 밀도 행렬 간의 평균 추적 거리를 통해 측정됩니다. MNIST 및 MedMNIST 데이터셋의 이진 분류 작업에서 수행된 벤치마크 테스트는 동일한 VQC 구조를 사용하면서도 훨씬 낮은 회로 깊이로 진폭 인코딩보다 상당한 성능 향상을 보여줍니다.

## 🎯 주요 포인트

- 1. 복잡한 데이터셋을 위한 효율적이고 데이터 중심적인 인코딩 방식이 제안되어 변분 양자 분류기의 성능을 향상시킵니다.

- 2. 제안된 인코딩은 힐베르트 공간에서 분류 레이블에 따라 잘 분리된 클러스터를 형성하는 입력 상태를 생성합니다.

- 3. 인코딩 회로는 고전적인 얼굴 인식 알고리즘에서 영감을 받은 트리플렛 손실 함수를 사용하여 훈련됩니다.

- 4. MNIST 및 MedMNIST 데이터셋의 이진 분류 작업에서 벤치마크 테스트 결과, 동일한 VQC 구조에서 진폭 인코딩보다 상당한 성능 향상을 보였습니다.

- 5. 제안된 인코딩 방식은 훨씬 낮은 회로 깊이를 요구하면서도 클래스 분리 가능성을 평균 추적 거리로 측정합니다.

---

*Generated on 2025-09-22 15:41:45*