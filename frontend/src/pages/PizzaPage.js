import {useEffect, useState} from "react";
import axios from "axios";
import {useSearchParams} from "react-router-dom";

const PizzaPage = () => {
    const [pizzas, setPizzas] = useState([]);
    const [pageInfo, setPageInfo] = useState({})
    const [searchParams, setSearchParams] = useSearchParams();
    const page = Number(searchParams.get('page')) || 1

    useEffect(() => {
        axios.get('api/pizza', {params: {page}}).then(({data}) => {
            setPizzas(data.data);
            setPageInfo({prev: data.prev, next: data.next});
        })
    }, [page]);
    return (
        <div>
            {
                pizzas.map(pizza => <div key={pizza.id}>{pizza.id}. {pizza.name}, {pizza.phone}</div>)
            }
            <button disabled={!pageInfo.prev} onClick={() => setSearchParams({page: page - 1})}>prev</button>
            <button disabled={!pageInfo.next} onClick={() => setSearchParams({page: page + 1})}>next</button>
        </div>
    );
};

export {
    PizzaPage
};
