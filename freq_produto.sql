with tb_freq_abs as (

    SELECT descProduto,
            count(idTransacao) as FreqAbs

    from points
    GROUP BY descProduto),

tb_freq_abs_acum as (

    select *,
            sum(FreqAbs) over (order by descProduto) as FreqAbsAcum,
            1.0 * FreqAbs / (SELECT sum(FreqAbs) from tb_freq_abs) as FreqRelativa
    from tb_freq_abs
)

SELECT *,
        sum(FreqRelativa) over (ORDER by descProduto) as FreqRelAcumulada
from tb_freq_abs_acum