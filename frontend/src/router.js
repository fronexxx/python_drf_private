import {createBrowserRouter, Navigate} from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import {PizzaPage} from "./pages/PizzaPage";

const router = createBrowserRouter([
    {
        path: '', element: <MainLayout/>, children: [
            {index: true, element: <Navigate to={'pizza'}/>},
            {path: 'pizza', element: <PizzaPage/>}
        ]
    }
])

export {router}