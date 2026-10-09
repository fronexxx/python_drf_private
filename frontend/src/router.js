import {createBrowserRouter, Navigate} from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import {ContactsPage} from "./pages/ContactsPage";

const router = createBrowserRouter([
    {
        path: '', element: <MainLayout/>, children: [
            {index: true, element: <Navigate to={'contacts'}/>},
            {path: 'contacts', element: <ContactsPage/>}
        ]
    }
])

export {router}