# Where Do Tokens Go? Understanding Pruning Behaviors in STEP at High Resolutions

**Korean Title:** 토큰은 어디로 가는가? 고해상도에서 STEP의 가지치기 동작 이해하기

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Michal Szczepanski|Michal Szczepanski]] [[authors/Martyna Poreba|Martyna Poreba]] [[authors/Karim Haroun|Karim Haroun]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Dynamic Patch Merging

## 🔗 유사한 논문
- [[AToken_ A Unified Tokenizer for Vision_20250919|AToken A Unified Tokenizer for Vision]] (80.9% similar)
- [[STEP_ Structured Training and Evaluation Platform for benchmarking trajectory prediction models_20250919|STEP Structured Training and Evaluation Platform for benchmarking trajectory prediction models]] (79.8% similar)
- [[Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (78.6% similar)
- [[[Re] Improving Interpretation Faithfulness for Vision Transformers_20250918|[Re] Improving Interpretation Faithfulness for Vision Transformers]] (78.5% similar)
- [[Communication Efficient Split Learning of ViTs with Attention-based Double Compression_20250919|Communication Efficient Split Learning of ViTs with Attention-based Double Compression]] (78.3% similar)

## 📋 저자 정보

**Authors:** Michal Szczepanski, Martyna Poreba, Karim Haroun

## 📄 Abstract (원문)

Vision Transformers (ViTs) achieve state-of-the-art performance in semantic
segmentation but are hindered by high computational and memory costs. To
address this, we propose STEP (SuperToken and Early-Pruning), a hybrid
token-reduction framework that combines dynamic patch merging and token pruning
to enhance efficiency without significantly compromising accuracy. At the core
of STEP is dCTS, a lightweight CNN-based policy network that enables flexible
merging into superpatches. Encoder blocks integrate also early-exits to remove
high-confident supertokens, lowering computational load. We evaluate our method
on high-resolution semantic segmentation benchmarks, including images up to
1024 x 1024, and show that when dCTS is applied alone, the token count can be
reduced by a factor of 2.5 compared to the standard 16 x 16 pixel patching
scheme. This yields a 2.6x reduction in computational cost and a 3.4x increase
in throughput when using ViT-Large as the backbone. Applying the full STEP
framework further improves efficiency, reaching up to a 4x reduction in
computational complexity and a 1.7x gain in inference speed, with a maximum
accuracy drop of no more than 2.0%. With the proposed STEP configurations, up
to 40% of tokens can be confidently predicted and halted before reaching the
final encoder layer.

## 🔍 Abstract (한글 번역)

비전 트랜스포머(ViTs)는 의미론적 분할에서 최첨단 성능을 달성하지만, 높은 계산 및 메모리 비용으로 인해 제약을 받습니다. 이를 해결하기 위해, 우리는 효율성을 높이면서 정확성을 크게 손상시키지 않는 동적 패치 병합과 토큰 가지치기를 결합한 하이브리드 토큰 감소 프레임워크인 STEP(SuperToken and Early-Pruning)을 제안합니다. STEP의 핵심은 유연한 병합을 가능하게 하는 경량 CNN 기반 정책 네트워크인 dCTS로, 이를 통해 슈퍼패치로의 병합을 수행합니다. 인코더 블록은 또한 높은 신뢰도의 슈퍼토큰을 제거하여 계산 부하를 줄이는 조기 종료를 통합합니다. 우리는 1024 x 1024까지의 이미지 등 고해상도 의미론적 분할 벤치마크에서 우리의 방법을 평가하였으며, dCTS를 단독으로 적용할 때 토큰 수가 표준 16 x 16 픽셀 패칭 방식에 비해 2.5배 감소할 수 있음을 보여주었습니다. 이는 ViT-Large를 백본으로 사용할 때 계산 비용을 2.6배 줄이고 처리량을 3.4배 증가시킵니다. 전체 STEP 프레임워크를 적용하면 효율성이 더욱 향상되어 계산 복잡도가 최대 4배 감소하고 추론 속도가 1.7배 증가하며, 최대 정확도 감소는 2.0%를 넘지 않습니다. 제안된 STEP 구성으로, 최대 40%의 토큰이 최종 인코더 레이어에 도달하기 전에 신뢰성 있게 예측되고 중단될 수 있습니다.

## 📝 요약

Vision Transformers(ViTs)는 뛰어난 성능을 보이지만 높은 계산 및 메모리 비용이 문제입니다. 이를 해결하기 위해 STEP(SuperToken and Early-Pruning)이라는 하이브리드 토큰 감소 프레임워크를 제안합니다. STEP는 동적 패치 병합과 토큰 프루닝을 결합하여 효율성을 높입니다. 핵심은 dCTS라는 경량 CNN 기반 정책 네트워크로, 유연한 슈퍼패치 병합을 가능하게 합니다. 또한, 인코더 블록에서 고신뢰도 슈퍼토큰을 조기에 제거하여 계산 부담을 줄입니다. 실험 결과, dCTS만으로도 토큰 수를 2.5배 줄이고, 계산 비용을 2.6배 줄이며, 처리량을 3.4배 증가시켰습니다. 전체 STEP 프레임워크를 적용하면 계산 복잡성은 4배 감소하고 추론 속도는 1.7배 증가하며, 정확도 손실은 최대 2.0%에 불과합니다. 제안된 STEP 구성으로 최대 40%의 토큰을 최종 인코더 레이어 전에 예측 및 중지할 수 있습니다.

## 🎯 주요 포인트

- 1. Vision Transformers의 높은 연산 및 메모리 비용 문제를 해결하기 위해 STEP(슈퍼토큰 및 초기-프루닝) 프레임워크를 제안합니다.

- 2. STEP의 핵심은 dCTS라는 경량 CNN 기반 정책 네트워크로, 유연한 슈퍼패치 병합을 가능하게 합니다.

- 3. STEP 프레임워크는 최대 4배의 연산 복잡도 감소와 1.7배의 추론 속도 향상을 이루며, 정확도 손실은 최대 2.0%에 불과합니다.

- 4. dCTS를 단독으로 적용할 경우, 토큰 수가 2.5배 감소하며, 연산 비용은 2.6배 줄고 처리량은 3.4배 증가합니다.

- 5. STEP 구성으로 최대 40%의 토큰이 최종 인코더 레이어에 도달하기 전에 자신 있게 예측 및 중단될 수 있습니다.

---

*Generated on 2025-09-20 07:45:52*