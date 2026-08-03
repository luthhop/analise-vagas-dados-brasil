SELECT
  modalidade,
  COUNT(*) AS total_vagas,
  ROUND(AVG(salario_medio), 2) AS salario_medio
FROM vagas
GROUP BY modalidade
ORDER BY total_vagas DESC;
