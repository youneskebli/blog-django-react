import {Link, Navigate, Outlet} from "react-router-dom";
import cookies from "../lib/cookies.ts";

const Layout = () => {
    if (!cookies.getCookie("access_token")) return <Navigate to="/login" />;
  return (
    <div className="pr-64 flex items-start w-full">
      <ul className="menu bg-base-200 h-screen w-56 py-20">
        <li className="text-xl">
          <Link to="/">Writers</Link>
        </li>
        <li className="text-xl">
          <Link to="/articles">Articles</Link>
        </li>
        <li className="text-xl">
          <Link to="/articles-edited">Edited Articles</Link>
        </li>
        <li className="text-xl">
          <Link to="/add-article">Add article</Link>
        </li>

        <li className="text-xl mt-10 pl-4" onClick={() => {
          cookies.deleteCookie("access_token")
          window.location.assign("/login")
        }}>
          Logout
        </li>
      </ul>
      <div className="py-20 px-10 w-full">
        <Outlet />
      </div>
    </div>
  );
};

export default Layout;
