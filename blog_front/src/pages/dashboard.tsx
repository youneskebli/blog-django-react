import { useQuery } from "@tanstack/react-query";
import { getWriters } from "../api/writer";
import Writer from "../domain/writer";
import WritersTable from "../components/writers-table";

const Dashboard = () => {
  const {
    data: writers,
    error,
    isError,
    isLoading,
  } = useQuery<Writer[], Error>({
    queryKey: ["articles"],
    queryFn: getWriters,
  });

  // if (isLoading) return "Loading ...";
  // if (isError) return <p className="text-error">{error?.message}</p>;
  return (
    <>
      <div className="breadcrumbs text-sm mb-10">
        <ul>
          <li>Dashboard</li>
        </ul>
      </div>
      <h1 className="text-3xl font-bold mb-10">Writers</h1>
      <WritersTable writers={writers || []} />
    </>
  );
};

export default Dashboard;
