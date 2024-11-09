import { Link, Outlet } from "react-router-dom";

const Layout = () => {
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
          <Link to="/add-article">Add article</Link>
        </li>
      </ul>
      <div className="py-20 px-10 w-full">
        <Outlet />
      </div>
    </div>
  );
};

export default Layout;
