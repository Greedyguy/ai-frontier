# G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving

**Korean Title:** G2D2: 역문제 해결을 위한 그래디언트 유도 이산 확산

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Discrete Diffusion Models, Continuous Relaxation Techniques

## 🔗 유사한 논문
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (83.1% similar)
- [[2025-09-17/Defending Diffusion Models Against Membership Inference Attacks via Higher-Order Langevin Dynamics_20250917|Defending Diffusion Models Against Membership Inference Attacks via Higher-Order Langevin Dynamics]] (83.0% similar)
- [[2025-09-19/End4_ End-to-end Denoising Diffusion for Diffusion-Based Inpainting Detection_20250919|End4 End-to-end Denoising Diffusion for Diffusion-Based Inpainting Detection]] (82.3% similar)
- [[2025-09-18/Generative Image Coding with Diffusion Prior_20250918|Generative Image Coding with Diffusion Prior]] (81.7% similar)
- [[2025-09-18/Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning_20250918|Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning]] (81.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.14710v2 Announce Type: replace-cross 
Abstract: Recent literature has effectively leveraged diffusion models trained on continuous variables as priors for solving inverse problems. Notably, discrete diffusion models with discrete latent codes have shown strong performance, particularly in modalities suited for discrete compressed representations, such as image and motion generation. However, their discrete and non-differentiable nature has limited their application to inverse problems formulated in continuous spaces. This paper presents a novel method for addressing linear inverse problems by leveraging generative models based on discrete diffusion as priors. We overcome these limitations by approximating the true posterior distribution with a variational distribution constructed from categorical distributions and continuous relaxation techniques. Furthermore, we employ a star-shaped noise process to mitigate the drawbacks of traditional discrete diffusion models with absorbing states, demonstrating that our method performs comparably to continuous diffusion techniques with a lower GPU memory consumption. Our code is available at https://github.com/sony/g2d2.

## 🔍 Abstract (한글 번역)

arXiv:2410.14710v2 발표 유형: 교체-크로스  
요약: 최근 문헌에서는 연속 변수에 대해 훈련된 확산 모델을 선행 분포로 활용하여 역문제를 해결하는 데 효과적으로 사용되었습니다. 특히, 이산 잠재 코드를 사용하는 이산 확산 모델은 이미지 및 모션 생성과 같은 이산 압축 표현에 적합한 모달리티에서 강력한 성능을 보여주었습니다. 그러나 이산적이고 비미분 가능한 특성으로 인해 연속 공간에서 형성된 역문제에의 적용이 제한되었습니다. 본 논문에서는 이산 확산을 기반으로 한 생성 모델을 선행 분포로 활용하여 선형 역문제를 해결하는 새로운 방법을 제시합니다. 우리는 범주형 분포와 연속 이완 기법으로 구성된 변분 분포를 사용하여 실제 사후 분포를 근사함으로써 이러한 제한을 극복합니다. 또한, 흡수 상태를 가진 전통적인 이산 확산 모델의 단점을 완화하기 위해 별 모양의 노이즈 프로세스를 사용하여, 우리의 방법이 연속 확산 기법과 비교할 만한 성능을 보이면서도 GPU 메모리 소비가 낮음을 입증합니다. 우리의 코드는 https://github.com/sony/g2d2에서 확인할 수 있습니다.

## 📝 요약

이 논문은 선형 역문제를 해결하기 위해 이산 확산 모델을 사전으로 활용하는 새로운 방법을 제안합니다. 기존의 이산 확산 모델은 비연속적 특성 때문에 연속 공간에서의 역문제에 적용하기 어려웠으나, 본 연구에서는 범주형 분포와 연속적 완화 기법을 사용하여 실제 사후 분포를 근사함으로써 이 문제를 해결했습니다. 또한, 전통적인 이산 확산 모델의 흡수 상태 문제를 완화하기 위해 별 모양의 노이즈 프로세스를 도입했습니다. 그 결과, 제안된 방법은 연속 확산 기법과 유사한 성능을 보이면서도 GPU 메모리 소비를 줄였습니다. 연구의 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 연속 변수에 대한 확산 모델을 활용한 기존 연구와 달리, 본 논문은 이산 확산 모델을 활용하여 선형 역문제를 해결하는 새로운 방법을 제안합니다.

- 2. 이산 확산 모델의 비연속적 특성을 극복하기 위해 범주형 분포와 연속적 완화 기법을 사용하여 근사적 사후 분포를 구성합니다.

- 3. 전통적인 이산 확산 모델의 흡수 상태 문제를 해결하기 위해 별 모양의 노이즈 프로세스를 도입하여 GPU 메모리 소비를 줄이면서도 연속 확산 기법과 유사한 성능을 보입니다.

- 4. 제안된 방법은 이미지 및 모션 생성과 같은 이산 압축 표현에 적합한 모달리티에서 강력한 성능을 발휘합니다.

- 5. 연구의 코드는 https://github.com/sony/g2d2에서 공개되어 있습니다.

---

*Generated on 2025-09-22 14:39:40*