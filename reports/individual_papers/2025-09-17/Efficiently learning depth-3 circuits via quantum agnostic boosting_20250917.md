# Efficiently learning depth-3 circuits via quantum agnostic boosting

**Korean Title:** 깊이-3 회로를 효율적으로 학습하기 위한 양자 비판적 부스팅

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Srinivasan Arunachalam|Srinivasan Arunachalam]] [[authors/Arkopal Dutt|Arkopal Dutt]] [[authors/Alexandru Gheorghiu|Alexandru Gheorghiu]] [[authors/Michael de Oliveira|Michael de Oliveira]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⭐ Unique Technical**: Quantum Agnostic Boosting

## 🔗 유사한 논문
- [[Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (80.8% similar)
- [[Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit_20250918|Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit]] (79.4% similar)
- [[Gap-Dependent Bounds for Federated $Q$-learning_20250919|Gap-Dependent Bounds for Federated $Q$-learning]] (77.6% similar)
- [[Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (77.2% similar)
- [[Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (77.1% similar)

## 📋 저자 정보

**Authors:** Srinivasan Arunachalam, Arkopal Dutt, Alexandru Gheorghiu, Michael de Oliveira

## 📄 Abstract (원문)

We initiate the study of quantum agnostic learning of phase states with
respect to a function class $\mathsf{C}\subseteq \{c:\{0,1\}^n\rightarrow
\{0,1\}\}$: given copies of an unknown $n$-qubit state $|\psi\rangle$ which has
fidelity $\textsf{opt}$ with a phase state
$|\phi_c\rangle=\frac{1}{\sqrt{2^n}}\sum_{x\in \{0,1\}^n}(-1)^{c(x)}|x\rangle$
for some $c\in \mathsf{C}$, output $|\phi\rangle$ which has fidelity $|\langle
\phi | \psi \rangle|^2 \geq \textsf{opt}-\varepsilon$. To this end, we give
agnostic learning protocols for the following classes: (i) Size-$t$ decision
trees which runs in time $\textsf{poly}(n,t,1/\varepsilon)$. This also implies
$k$-juntas can be agnostically learned in time
$\textsf{poly}(n,2^k,1/\varepsilon)$. (ii) $s$-term DNF formulas in
near-polynomial time $\textsf{poly}(n,(s/\varepsilon)^{\log \log
s/\varepsilon})$.
  Our main technical contribution is a quantum agnostic boosting protocol which
converts a weak agnostic learner, which outputs a parity state $|\phi\rangle$
such that $|\langle \phi|\psi\rangle|^2\geq \textsf{opt}/\textsf{poly}(n)$,
into a strong learner which outputs a superposition of parity states
$|\phi'\rangle$ such that $|\langle \phi'|\psi\rangle|^2\geq \textsf{opt} -
\varepsilon$.
  Using quantum agnostic boosting, we obtain the first near-polynomial time
$n^{O(\log \log n)}$ algorithm for learning $\textsf{poly}(n)$-sized depth-$3$
circuits (consisting of $\textsf{AND}$, $\textsf{OR}$, $\textsf{NOT}$ gates) in
the uniform quantum $\textsf{PAC}$ model using quantum examples. Classically,
the analogue of efficient learning depth-$3$ circuits (and even depth-$2$
circuits) in the uniform $\textsf{PAC}$ model has been a longstanding open
question in computational learning theory. Our work nearly settles this
question, when the learner is given quantum examples.

## 🔍 Abstract (한글 번역)

양자 비판적 학습(agnostic learning)에서 함수 클래스 $\mathsf{C}\subseteq \{c:\{0,1\}^n\rightarrow \{0,1\}\}$에 대한 위상 상태(phase state)의 학습을 시작합니다. 이는 어떤 $c\in \mathsf{C}$에 대해 위상 상태 $|\phi_c\rangle=\frac{1}{\sqrt{2^n}}\sum_{x\in \{0,1\}^n}(-1)^{c(x)}|x\rangle$와의 적합도(fidelity)가 $\textsf{opt}$인 미지의 $n$-큐빗 상태 $|\psi\rangle$의 복사본을 주어진 상황에서, 적합도 $|\langle \phi | \psi \rangle|^2 \geq \textsf{opt}-\varepsilon$를 갖는 $|\phi\rangle$를 출력하는 것을 목표로 합니다. 이를 위해, 우리는 다음 클래스에 대한 비판적 학습 프로토콜을 제시합니다: (i) 시간 복잡도가 $\textsf{poly}(n,t,1/\varepsilon)$인 크기-$t$ 결정 트리. 이는 또한 $k$-juntas를 시간 복잡도 $\textsf{poly}(n,2^k,1/\varepsilon)$로 비판적으로 학습할 수 있음을 의미합니다. (ii) 거의 다항 시간 $\textsf{poly}(n,(s/\varepsilon)^{\log \log s/\varepsilon})$ 내에 $s$-항 DNF 공식.

우리의 주요 기술적 기여는 약한 비판적 학습자를 강한 학습자로 변환하는 양자 비판적 부스팅 프로토콜입니다. 이 프로토콜은 $|\langle \phi|\psi\rangle|^2\geq \textsf{opt}/\textsf{poly}(n)$인 패리티 상태 $|\phi\rangle$를 출력하는 약한 비판적 학습자를, $|\langle \phi'|\psi\rangle|^2\geq \textsf{opt} - \varepsilon$인 패리티 상태의 중첩 상태 $|\phi'\rangle$를 출력하는 강한 학습자로 변환합니다.

양자 비판적 부스팅을 사용하여, 우리는 양자 예제를 사용하는 균일 양자 $\textsf{PAC}$ 모델에서 $\textsf{poly}(n)$ 크기의 깊이-$3$ 회로($\textsf{AND}$, $\textsf{OR}$, $\textsf{NOT}$ 게이트로 구성됨)를 학습하는 첫 번째 거의 다항 시간 $n^{O(\log \log n)}$ 알고리즘을 얻습니다. 고전적으로, 균일 $\textsf{PAC}$ 모델에서 깊이-$3$ 회로(심지어 깊이-$2$ 회로)의 효율적 학습에 대한 유사한 문제는 계산 학습 이론에서 오랜 미해결 문제였습니다. 우리의 연구는 학습자가 양자 예제를 제공받는 경우, 이 문제를 거의 해결합니다.

## 📝 요약

이 논문은 함수 클래스 $\mathsf{C}$에 대한 위상 상태의 양자 비판적 학습을 연구합니다. 주어진 $n$-큐빗 상태 $|\psi\rangle$가 위상 상태 $|\phi_c\rangle$와의 충실도가 $\textsf{opt}$일 때, 충실도가 $\textsf{opt}-\varepsilon$ 이상인 $|\phi\rangle$를 출력하는 방법을 제시합니다. 주요 기여는 약한 학습자를 강한 학습자로 변환하는 양자 비판적 부스팅 프로토콜 개발입니다. 이를 통해 크기 $t$의 결정 트리와 $s$-항 DNF 공식을 효율적으로 학습할 수 있으며, 특히 깊이 3의 회로를 양자 PAC 모델에서 거의 다항 시간 내에 학습할 수 있는 알고리즘을 제안합니다. 이는 고전적인 PAC 모델에서 해결되지 않은 문제에 대한 중요한 진전을 이룹니다.

## 🎯 주요 포인트

- 1. 양자 무관 학습을 통해 위상 상태를 학습하는 새로운 방법을 제안하였습니다.

- 2. 크기-$t$ 결정 트리를 다루는 무관 학습 프로토콜을 개발하여, $k$-juntas를 효율적으로 학습할 수 있음을 보였습니다.

- 3. $s$-항 DNF 공식을 거의 다항 시간 내에 학습할 수 있는 방법을 제시하였습니다.

- 4. 약한 무관 학습자를 강한 학습자로 변환하는 양자 무관 부스팅 프로토콜을 개발하였습니다.

- 5. 양자 예제를 사용하여 깊이-3 회로를 학습하는 첫 번째 거의 다항 시간 알고리즘을 제안하였으며, 이는 전통적인 컴퓨팅 학습 이론에서의 오랜 문제를 해결하는 데 기여하였습니다.

---

*Generated on 2025-09-20 05:55:38*