# X ~ N(3, 7^2)

from scipy.stats import norm

x=norm.ppf(0.25, loc=3, scale=7)
z=norm.ppf(0.25, loc=0, scale=1)

x
3 + z * 7

norm.cdf(5, loc=3, scale=7)
norm.cdf(2/7, loc=0, scale=1)

norm.ppf(0.975, loc=0, scale=1)


z=norm.rvs(loc=0, scale=1, size=1000)
z

x=z*np.sqrt(2) + 3
sns.histplot(z, stat="density", color="grey")
sns.histplot(x, stat="density", color="green")

# Plot the normal distribution PDF
zmin, zmax = (z.min(), x.max())
z_values = np.linspace(zmin, zmax, 500)
pdf_values = norm.pdf(z_values, loc=0, scale=1)
pdf_values2 = norm.pdf(z_values, loc=3, scale=np.sqrt(2))
plt.plot(z_values, pdf_values, color='red', linewidth=2)
plt.plot(z_values, pdf_values2, color='blue', linewidth=2)

plt.show()
plt.clf()


# 표준화 확인
x=norm.rvs(loc=5, scale=3, size=1000)

# 표준화
z=(x - 5)/3
sns.histplot(z, stat="density", color="grey")

# Plot the normal distribution PDF
zmin, zmax = (z.min(), z.max())
z_values = np.linspace(zmin, zmax, 100)
pdf_values = norm.pdf(z_values, loc=0, scale=1)
plt.plot(z_values, pdf_values, color='red', linewidth=2)

plt.show()
plt.clf()


# 표본표준편차 나눠도 표준정규분포가 될까?
#1.
x=norm.rvs(loc=5, scale=3, size=20)
s=np.std(x, ddof=1)
s
# s_2=np.var(x, ddof=1)

#2.
x=norm.rvs(loc=5, scale=3, size=1000)

# 표준화
z=(x - 5)/s
# z=(x - 5)/3
sns.histplot(z, stat="density", color="grey")

# Plot the normal distribution PDF
zmin, zmax = (z.min(), z.max())
z_values = np.linspace(zmin, zmax, 100)
pdf_values = norm.pdf(z_values, loc=0, scale=1)
plt.plot(z_values, pdf_values, color='red', linewidth=2)

plt.show()
plt.clf()

# t 분포에 대해서 알아보자!
# X ~ t(n)
# 종모양, 대칭분포, 중심 0
# 모수 n: 자유도라고 부름 - 퍼짐을 나타내는 모수
# n 이 작으면 분산 커짐.
# n 이 무한대로 가면 표준정규분포가 된다.
from scipy.stats import t

# t.pdf
# t.ppf
# t.cdf
# t.rvs
# 자유도가 4인 t분포의 pdf를 그려보세요!
t_values = np.linspace(-4, 4, 100)
pdf_values = t.pdf(t_values, df=30)
plt.plot(t_values, pdf_values, color='red', linewidth=2)
# 표준정규분포 겹치기
pdf_values = norm.pdf(t_values, loc=0, scale=1)
plt.plot(t_values, pdf_values, color='black', linewidth=2)

plt.show()
plt.clf()

# X ~ ?(mu, sigma^2)
# X bar ~ N(mu, sigma^2/n)
# X bar ~= t(x_bar, s^2/n) 자유도가 n-1인 t 분포
x=norm.rvs(loc=15, scale=3, size=16, random_state=42)
x
x_bar=x.mean()
n=len(x)

# df=degree of freedom
# 모분산을 모를때: 모평균에 대한 95% 신뢰구간을 구해보자!
x_bar + t.ppf(0.975, df=n-1) * np.std(x, ddof=1) / np.sqrt(n)
x_bar - t.ppf(0.975, df=n-1) * np.std(x, ddof=1) / np.sqrt(n)

# 모분산(3^2)을 알때: 모평균에 대한 95% 신뢰구간을 구해보자!
x_bar + norm.ppf(0.975, loc=0, scale=1) * 3 / np.sqrt(n)
x_bar - norm.ppf(0.975, loc=0, scale=1) * 3 / np.sqrt(n)










