### UPDATED by MILAN 07.06. - change: converted simple plots to version with functions
### UPDATED by MILAN 15.09. - change: created new database

### ----------- FUNCTION TOTAL COSTS  -----------------------------------------
def total_costs(path_name,topic_name, year_name, group_type):
    
    # choose directory where the files and grpahs produced in this function will be stored
    folder_name = "total_costs"
    path_name = path_name + folder_name
    if not os.path.exists(path_name):
        os.mkdir(path_name)
    os.chdir(path_name)

    # Create the file and ready it for appending the data
    x_axis_file = open('x_axis_file.txt', mode='a+')

    if group_type == "coordination":
        if topic_name=="ALL":
            # queries for participants and coordinators for ALL calls and years
            # this part of query "sum([Total costs]) total_costs," goes through all data in column Total costs and makes sum and finally put that value in total_costs parameter
            sql = """ SELECT sum([Total costs]) total_costs, Country, [Participant role] role, Status FROM Annex7T7_new WHERE Status=='Main list' AND role == 'Coordinator' GROUP BY Country ORDER BY total_costs DESC"""
            data_coo = pd.read_sql(sql, conn)
            sql = """ SELECT sum([Total costs]) total_costs, Country, [Participant role] role, Status FROM Annex7T7_new WHERE Status=='Main list' AND role LIKE 'Participant%' GROUP BY Country ORDER BY total_costs DESC"""
            data_part = pd.read_sql(sql, conn)
            colors = {'Coordinators':'tab:blue', 'Participants':'tab:orange'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(14,6))
            plt.bar(data_coo.Country, data_coo.total_costs,color='tab:blue',align='edge',width=-0.4)
            plt.bar(data_part.Country, data_part.total_costs,color='tab:orange',align='edge',width=0.4)
            plt.ticklabel_format(axis='Y', style = 'sci', useMathText=True)
            plt.title("Total costs: all calls - funded projects")
            plt.legend(handles, labels)
            name_graph="total_costs_all_calls.png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data_coo.Country.to_string(index=False).split("\n")
            second_axis=data_part.Country.to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments
            sql = """ SELECT sum([Total costs]) total_costs, Country, [Participant role] role, Status FROM Annex7T7_new WHERE Status=='Main list' AND role == 'Coordinator' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_costs DESC"""
            data_coo = pd.read_sql(sql, conn)
            sql = """ SELECT sum([Total costs]) total_costs, Country, [Participant role] role, Status FROM Annex7T7_new WHERE Status=='Main list' AND role LIKE 'Participant%' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_costs DESC"""
            data_part = pd.read_sql(sql, conn)
            colors = {'Coordinators':'tab:blue', 'Participants':'tab:orange'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(14,6))
            plt.bar(data_coo.Country, data_coo.total_costs,color='tab:blue',align='edge',width=-0.4)  #alpha=0.5
            plt.bar(data_part.Country, data_part.total_costs,color='tab:orange',align='edge',width=0.4)  #alpha=0.5
            plt.ticklabel_format(axis='Y', style = 'sci', useMathText=True)
            plt.title("Total costs: " + topic_name + year_name + " - funded projects")
            plt.legend(handles, labels)
            name_graph = "total_costs_"+topic_name+year_name+".png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data_coo.Country.to_string(index=False).split("\n")
            second_axis=data_part.Country.to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

    elif group_type == "division_eu":
        if topic_name=="ALL":
            sql = """ SELECT sum([Total costs]) total_costs, Country, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' GROUP BY Country ORDER BY total_costs DESC"""
            data = pd.read_sql(sql, conn)
            plt.figure(figsize=(14,6))
            colors = {'EU14':'tab:blue', 'EU13':'tab:orange', 'AC':'tab:green', 'OTH':'tab:grey'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.bar(data.Country[data.division_eu=='EU14'], data.total_costs[data.division_eu=='EU14'],color=colors['EU14'])
            plt.bar(data.Country[data.division_eu=='EU13'], data.total_costs[data.division_eu=='EU13'],color=colors['EU13'])
            plt.bar(data.Country[data.division_eu=='AC'], data.total_costs[data.division_eu=='AC'],color=colors['AC'])
            plt.bar(data.Country[data.division_eu=='OTH'], data.total_costs[data.division_eu=='OTH'],color=colors['OTH'])
            plt.ticklabel_format(axis='Y', style = 'sci', useMathText=True)
            plt.title("Total costs: all calls - per group - funded projects")
            plt.legend(handles, labels)
            name_graph="total_costs_groups_all_calls.png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data.Country[data.division_eu=='EU14'].to_string(index=False).split("\n")
            second_axis=data.Country[data.division_eu=='EU13'].to_string(index=False).split("\n")
            third_axis=data.Country[data.division_eu=='AC'].to_string(index=False).split("\n")
            fourth_axis=data.Country[data.division_eu=='OTH'].to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis + third_axis + fourth_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments
            sql = """ SELECT sum([Total costs]) total_costs, Country, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_costs DESC"""
            data = pd.read_sql(sql, conn)
            plt.figure(figsize=(14,6))
            colors = {'EU14':'tab:blue', 'EU13':'tab:orange', 'AC':'tab:green', 'OTH':'tab:grey'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.bar(data.Country[data.division_eu=='EU14'], data.total_costs[data.division_eu=='EU14'],color=colors['EU14'])
            plt.bar(data.Country[data.division_eu=='EU13'], data.total_costs[data.division_eu=='EU13'],color=colors['EU13'])
            plt.bar(data.Country[data.division_eu=='AC'], data.total_costs[data.division_eu=='AC'],color=colors['AC'])
            plt.bar(data.Country[data.division_eu=='OTH'], data.total_costs[data.division_eu=='OTH'],color=colors['OTH'])
            plt.ticklabel_format(axis='Y', style = 'sci', useMathText=True)
            plt.title("Total costs: per group " + topic_name + year_name + " - funded projects")
            plt.legend(handles, labels)
            name_graph="total_costs_groups_"+topic_name+year_name+".png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data.Country[data.division_eu=='EU14'].to_string(index=False).split("\n")
            second_axis=data.Country[data.division_eu=='EU13'].to_string(index=False).split("\n")
            third_axis=data.Country[data.division_eu=='AC'].to_string(index=False).split("\n")
            fourth_axis=data.Country[data.division_eu=='OTH'].to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis + third_axis + fourth_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

    elif group_type == "widening":
        if topic_name=="ALL":
            sql = """ SELECT sum([Total costs]) total_costs, Country, division_wd, Status FROM Annex7T7_new WHERE Status=='Main list' GROUP BY Country ORDER BY total_costs DESC"""
            data = pd.read_sql(sql, conn)
            plt.figure(figsize=(14,6))
            colors = {'WD':'tab:blue'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.bar(data.Country[data.division_wd=='WD'], data.total_costs[data.division_wd=='WD'],color=colors['WD'])
            plt.ticklabel_format(axis='Y', style = 'sci', useMathText=True)
            plt.title("Total costs: all calls - widening - funded projects")
            plt.legend(handles, labels)
            name_graph="total_costs_widening_all_calls.png"
            plt.savefig(name_graph, dpi=300)
            name_axes=data.Country[data.division_wd=='WD'].to_string(index=False).split("\n")
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments
            sql = """ SELECT sum([Total costs]) total_costs, Country, division_wd, Status FROM Annex7T7_new WHERE Status=='Main list' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_costs DESC"""
            data = pd.read_sql(sql, conn)
            plt.figure(figsize=(14,6))
            colors = {'WD':'tab:blue'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.bar(data.Country[data.division_wd=='WD'], data.total_costs[data.division_wd=='WD'],color=colors['WD'])
            plt.ticklabel_format(axis='Y', style = 'sci', useMathText=True)
            plt.title("Total costs: widening " + topic_name + year_name + " - funded projects")
            plt.legend(handles, labels)
            name_graph="total_costs_widening_"+topic_name+year_name+".png"
            plt.savefig(name_graph, dpi=300)
            name_axes=data.Country[data.division_wd=='WD'].to_string(index=False).split("\n")
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

    else:
        # finally if none of the options is matched then error statement is printed.
        print("ERROR - you have selected group_type that is not supported by this function.")

    x_axis_file.close()
### ------------ END OF FUNCTION TOTAL COSTS ----------------------------------





### ------------ FUNCTION PARTICIPATION COUNT ---------------------------------
def participation_count(path_name,topic_name, year_name, group_type):
  
    # choose directory where the files and grpahs produced in this function will be stored
    folder_name = "participation_count"
    path_name = path_name + folder_name
    if not os.path.exists(path_name):
        os.mkdir(path_name)
    os.chdir(path_name)
    x_axis_file = open('x_axis_file.txt', mode='a+')
    
    if group_type == "coordination":
        if topic_name=="ALL":
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, Status FROM Annex7T7_new WHERE Status=='Main list' AND role == 'Coordinator' GROUP BY Country ORDER BY total_num DESC"""
            data_count_coo = pd.read_sql(sql, conn)
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, Status FROM Annex7T7_new WHERE Status=='Main list' AND role LIKE 'Participant%' GROUP BY Country ORDER BY total_num DESC"""
            data_count_part = pd.read_sql(sql, conn)
            colors = {'Coordinators':'tab:blue', 'Participants':'tab:orange'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(14,6))
            plt.bar(data_count_coo.Country, data_count_coo['total_num'],color='tab:blue',align='edge',width=-0.4)
            plt.bar(data_count_part.Country, data_count_part['total_num'],color='tab:orange',align='edge',width=0.4)
            plt.title("Participation count: all calls - funded projects")
            plt.legend(handles, labels)
            name_graph="participation_count_all_calls.png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data_count_coo.Country.to_string(index=False).split("\n")
            second_axis=data_count_part.Country.to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments (both assigned before the first if statement)
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, Status FROM Annex7T7_new WHERE Status=='Main list' AND role == 'Coordinator' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_num DESC"""
            data_count_coo = pd.read_sql(sql, conn)
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, Status FROM Annex7T7_new WHERE Status=='Main list' AND role LIKE 'Participant%' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_num DESC"""
            data_count_part = pd.read_sql(sql, conn)
            colors = {'Coordinators':'tab:blue', 'Participants':'tab:orange'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(14,6))
            plt.bar(data_count_coo.Country, data_count_coo['total_num'],color='tab:blue',align='edge',width=-0.4)
            plt.bar(data_count_part.Country, data_count_part['total_num'],color='tab:orange',align='edge',width=0.4)
            plt.title("Participation count: " + topic_name + year_name + " - funded projects")
            plt.legend(handles, labels)
            name_graph="participation_count_"+topic_name+year_name+".png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data_count_coo.Country.to_string(index=False).split("\n")
            second_axis=data_count_part.Country.to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

    elif group_type == "coordination_EU14":
        if topic_name=="ALL":
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_eu=='EU14' AND role == 'Coordinator' GROUP BY Country ORDER BY total_num DESC"""
            data_count_coo = pd.read_sql(sql, conn)
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_eu=='EU14' AND role LIKE 'Participant%' GROUP BY Country ORDER BY total_num DESC"""
            data_count_part = pd.read_sql(sql, conn)
            colors = {'Coordinators':'tab:blue', 'Participants':'tab:orange'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(14,6))
            plt.bar(data_count_coo.Country, data_count_coo['total_num'],color='tab:blue',align='edge',width=-0.4)
            plt.bar(data_count_part.Country, data_count_part['total_num'],color='tab:orange',align='edge',width=0.4)
            plt.title("Participation count EU14 countries: all calls - funded projects")
            plt.legend(handles, labels)
            name_graph="participation_count_EU14_all_calls.png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data_count_coo.Country.to_string(index=False).split("\n")
            second_axis=data_count_part.Country.to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments (both assigned before the first if statement)
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_eu=='EU14' AND role == 'Coordinator' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_num DESC"""
            data_count_coo = pd.read_sql(sql, conn)
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_eu=='EU14' AND role LIKE 'Participant%' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_num DESC"""
            data_count_part = pd.read_sql(sql, conn)
            colors = {'Coordinators':'tab:blue', 'Participants':'tab:orange'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(14,6))
            plt.bar(data_count_coo.Country, data_count_coo['total_num'],color='tab:blue',align='edge',width=-0.4)
            plt.bar(data_count_part.Country, data_count_part['total_num'],color='tab:orange',align='edge',width=0.4)
            plt.title("Participation count - EU14 countries: " + topic_name + year_name + " - funded projects")
            plt.legend(handles, labels)
            name_graph="participation_count_EU14_"+topic_name+year_name+".png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data_count_coo.Country.to_string(index=False).split("\n")
            second_axis=data_count_part.Country.to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

    elif group_type == "coordination_EU13":
        if topic_name=="ALL":
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_eu=='EU13' AND role == 'Coordinator' GROUP BY Country ORDER BY total_num DESC"""
            data_count_coo = pd.read_sql(sql, conn)
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_eu=='EU13' AND role LIKE 'Participant%' GROUP BY Country ORDER BY total_num DESC"""
            data_count_part = pd.read_sql(sql, conn)
            colors = {'Coordinators':'tab:blue', 'Participants':'tab:orange'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(14,6))
            plt.bar(data_count_coo.Country, data_count_coo['total_num'],color='tab:blue',align='edge',width=-0.4)
            plt.bar(data_count_part.Country, data_count_part['total_num'],color='tab:orange',align='edge',width=0.4)
            plt.title("Participation count EU13 countries: all calls - funded projects")
            plt.legend(handles, labels)
            name_graph="participation_count_EU13_all_calls.png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data_count_coo.Country.to_string(index=False).split("\n")
            second_axis=data_count_part.Country.to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments (both assigned before the first if statement)
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_eu=='EU13' AND role == 'Coordinator' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_num DESC"""
            data_count_coo = pd.read_sql(sql, conn)
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_eu=='EU13' AND role LIKE 'Participant%' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_num DESC"""
            data_count_part = pd.read_sql(sql, conn)
            colors = {'Coordinators':'tab:blue', 'Participants':'tab:orange'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(14,6))
            plt.bar(data_count_coo.Country, data_count_coo['total_num'],color='tab:blue',align='edge',width=-0.4)
            plt.bar(data_count_part.Country, data_count_part['total_num'],color='tab:orange',align='edge',width=0.4)
            plt.title("Participation count - EU13 countries: " + topic_name + year_name + " - funded projects")
            plt.legend(handles, labels)
            name_graph="participation_count_EU13_"+topic_name+year_name+".png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data_count_coo.Country.to_string(index=False).split("\n")
            second_axis=data_count_part.Country.to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

    elif group_type == "coordination_AC":
        if topic_name=="ALL":
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_eu=='AC' AND role == 'Coordinator' GROUP BY Country ORDER BY total_num DESC"""
            data_count_coo = pd.read_sql(sql, conn)
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_eu=='AC' AND role LIKE 'Participant%' GROUP BY Country ORDER BY total_num DESC"""
            data_count_part = pd.read_sql(sql, conn)
            colors = {'Coordinators':'tab:blue', 'Participants':'tab:orange'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(14,6))
            plt.bar(data_count_coo.Country, data_count_coo['total_num'],color='tab:blue',align='edge',width=-0.4)
            plt.bar(data_count_part.Country, data_count_part['total_num'],color='tab:orange',align='edge',width=0.4)
            plt.title("Participation count AC countries: all calls - funded projects")
            plt.legend(handles, labels)
            name_graph="participation_count_AC_all_calls.png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data_count_coo.Country.to_string(index=False).split("\n")
            second_axis=data_count_part.Country.to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()
            
        else:
            # use topic_name and year_name from the function arguments (both assigned before the first if statement)
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_eu=='AC' AND role == 'Coordinator' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_num DESC"""
            data_count_coo = pd.read_sql(sql, conn)
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_eu=='AC' AND role LIKE 'Participant%' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_num DESC"""
            data_count_part = pd.read_sql(sql, conn)
            colors = {'Coordinators':'tab:blue', 'Participants':'tab:orange'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(14,6))
            plt.bar(data_count_coo.Country, data_count_coo['total_num'],color='tab:blue',align='edge',width=-0.4)
            plt.bar(data_count_part.Country, data_count_part['total_num'],color='tab:orange',align='edge',width=0.4)
            plt.title("Participation count - AC countries: " + topic_name + year_name + " - funded projects")
            plt.legend(handles, labels)
            name_graph="participation_count_AC_"+topic_name+year_name+".png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data_count_coo.Country.to_string(index=False).split("\n")
            second_axis=data_count_part.Country.to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

    elif group_type == "coordination_WD":
        if topic_name=="ALL":
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_wd, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_wd=='WD' AND role == 'Coordinator' GROUP BY Country ORDER BY total_num DESC"""
            data_count_coo = pd.read_sql(sql, conn)
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_wd, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_wd=='WD' AND role LIKE 'Participant%' GROUP BY Country ORDER BY total_num DESC"""
            data_count_part = pd.read_sql(sql, conn)
            colors = {'Coordinators':'tab:blue', 'Participants':'tab:orange'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(14,6))
            plt.bar(data_count_coo.Country, data_count_coo['total_num'],color='tab:blue',align='edge',width=-0.4)
            plt.bar(data_count_part.Country, data_count_part['total_num'],color='tab:orange',align='edge',width=0.4)
            plt.title("Participation count Widening countries: all calls - funded projects")
            plt.legend(handles, labels)
            name_graph="participation_count_WD_all_calls.png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data_count_coo.Country.to_string(index=False).split("\n")
            second_axis=data_count_part.Country.to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()
            
        else:
            # use topic_name and year_name from the function arguments (both assigned before the first if statement)
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_wd, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_wd=='WD' AND role == 'Coordinator' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_num DESC"""
            data_count_coo = pd.read_sql(sql, conn)
            sql = """ SELECT count(Country) total_num, Country, [Participant role] role, division_wd, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_wd=='WD' AND role LIKE 'Participant%' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_num DESC"""
            data_count_part = pd.read_sql(sql, conn)
            colors = {'Coordinators':'tab:blue', 'Participants':'tab:orange'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(14,6))
            plt.bar(data_count_coo.Country, data_count_coo['total_num'],color='tab:blue',align='edge',width=-0.4)
            plt.bar(data_count_part.Country, data_count_part['total_num'],color='tab:orange',align='edge',width=0.4)
            plt.title("Participation count - Widening countries: " + topic_name + year_name + " - funded projects")
            plt.legend(handles, labels)
            name_graph="participation_count_WD_"+topic_name+year_name+".png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data_count_coo.Country.to_string(index=False).split("\n")
            second_axis=data_count_part.Country.to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

    elif group_type == "division_eu":
        if topic_name=="ALL":            
            sql = """ SELECT count(Country) total_num, Country, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' GROUP BY Country ORDER BY total_num DESC"""
            data = pd.read_sql(sql, conn)
            plt.figure(figsize=(14,6))
            colors = {'EU14':'tab:blue', 'EU13':'tab:orange', 'AC':'tab:green', 'OTH':'tab:grey'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.bar(data.Country[data.division_eu=='EU14'], data.total_num[data.division_eu=='EU14'],color=colors['EU14'])
            plt.bar(data.Country[data.division_eu=='EU13'], data.total_num[data.division_eu=='EU13'],color=colors['EU13'])
            plt.bar(data.Country[data.division_eu=='AC'], data.total_num[data.division_eu=='AC'],color=colors['AC'])
            plt.bar(data.Country[data.division_eu=='OTH'], data.total_num[data.division_eu=='OTH'],color=colors['OTH'])
            plt.title("Participation count: all calls - per group - funded projects")
            plt.legend(handles, labels)
            name_graph="participation_count_groups_all_calls.png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data.Country[data.division_eu=='EU14'].to_string(index=False).split("\n")
            second_axis=data.Country[data.division_eu=='EU13'].to_string(index=False).split("\n")
            third_axis=data.Country[data.division_eu=='AC'].to_string(index=False).split("\n")
            fourth_axis=data.Country[data.division_eu=='OTH'].to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis + third_axis + fourth_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments
            sql = """ SELECT count(Country) total_num, Country, division_eu, Status FROM Annex7T7_new WHERE Status=='Main list' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_num DESC"""
            data = pd.read_sql(sql, conn)
            plt.figure(figsize=(14,6))
            colors = {'EU14':'tab:blue', 'EU13':'tab:orange', 'AC':'tab:green', 'OTH':'tab:grey'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.bar(data.Country[data.division_eu=='EU14'], data.total_num[data.division_eu=='EU14'],color=colors['EU14'])
            plt.bar(data.Country[data.division_eu=='EU13'], data.total_num[data.division_eu=='EU13'],color=colors['EU13'])
            plt.bar(data.Country[data.division_eu=='AC'], data.total_num[data.division_eu=='AC'],color=colors['AC'])
            plt.bar(data.Country[data.division_eu=='OTH'], data.total_num[data.division_eu=='OTH'],color=colors['OTH'])
            plt.title("Participation count: per group " + topic_name + year_name + " - funded projects")
            plt.legend(handles, labels)
            name_graph="participation_count_groups_"+topic_name+year_name+".png"
            plt.savefig(name_graph, dpi=300)
            first_axis=data.Country[data.division_eu=='EU14'].to_string(index=False).split("\n")
            second_axis=data.Country[data.division_eu=='EU13'].to_string(index=False).split("\n")
            third_axis=data.Country[data.division_eu=='AC'].to_string(index=False).split("\n")
            fourth_axis=data.Country[data.division_eu=='OTH'].to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis + third_axis + fourth_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()
                
    elif group_type=="widening":
        if topic_name=="ALL":
            sql = """ SELECT count(Country) total_num, Country, division_wd, Status FROM Annex7T7_new WHERE Status=='Main list' GROUP BY Country ORDER BY total_num DESC"""
            data = pd.read_sql(sql, conn)
            plt.figure(figsize=(14,6))
            colors = {'WD':'tab:blue'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.bar(data.Country[data.division_wd=='WD'], data.total_num[data.division_wd=='WD'],color=colors['WD'])
            plt.title("Participation count: all calls - widening - funded projects")
            plt.legend(handles, labels)
            name_graph="participation_count_widening_all_calls.png"
            plt.savefig(name_graph, dpi=300)
            name_axes=data.Country[data.division_wd=='WD'].to_string(index=False).split("\n")
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments
            sql = """ SELECT count(Country) total_num, Country, division_wd, Status FROM Annex7T7_new WHERE Status=='Main list' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY Country ORDER BY total_num DESC"""
            data = pd.read_sql(sql, conn)
            plt.figure(figsize=(14,6))
            colors = {'WD':'tab:blue'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.bar(data.Country[data.division_wd=='WD'], data.total_num[data.division_wd=='WD'],color=colors['WD'])
            plt.title("Participation count: widening " + topic_name + year_name + " - funded projects")
            plt.legend(handles, labels)
            name_graph="participation_count_widening_"+topic_name+year_name+".png"
            plt.savefig(name_graph, dpi=300)
            name_axes=data.Country[data.division_wd=='WD'].to_string(index=False).split("\n")
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()
        
    else:
        # finally if none of the options is matched then error statement is printed.
        print("ERROR - you have selected group_type that is not supported by this function.")
    
    x_axis_file.close()

### ------------ END OF FUNCTION PARTICIPATION COUNT --------------------------





### ------------ FUNCTION LEGAL TYPE ------------------------------------------
def legal_type(path_name,topic_name, year_name, group_type):
  
    # choose directory where the files and grpahs produced in this function will be stored
    folder_name = "legal_type"
    path_name = path_name + folder_name
    if not os.path.exists(path_name):
        os.mkdir(path_name)
    os.chdir(path_name)
    x_axis_file = open('x_axis_file.txt', mode='a+')

    # this graph is printed always, simply because it does not have any conditions.
    sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, Status FROM Annex7T7_new WHERE Status=="Main list" GROUP BY legal_type ORDER BY legal_type_count DESC"""
    data = pd.read_sql(sql, conn)
    plt.figure(figsize=(16,6))
    plt.bar(data.legal_type, data.legal_type_count,color='tab:green')
    plt.title("Participation by legal type: all calls - funded projects")
    name_graph="legal_type_all_calls.png"
    plt.savefig(name_graph, dpi=300)
    plt.close()
        
    if group_type == "coordination":
        if topic_name=="ALL":
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, [Participant role] role, Status FROM Annex7T7_new WHERE Status=='Main list' AND role == 'Coordinator' GROUP BY legal_type ORDER BY legal_type_count DESC"""
            data_coo = pd.read_sql(sql, conn)
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, [Participant role] role, Status FROM Annex7T7_new WHERE Status=='Main list' AND role LIKE 'Participant%' GROUP BY legal_type ORDER BY legal_type_count DESC"""
            data_part = pd.read_sql(sql, conn)
            colors = {'Coordinators':'tab:blue', 'Participants':'tab:orange'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(16,6))
            plt.bar(data_coo.legal_type, data_coo.legal_type_count, color='tab:blue',align='edge',width=-0.4)
            plt.bar(data_part.legal_type, data_part.legal_type_count, color='tab:orange',align='edge',width=0.4)
            plt.title("Participation by legal type: all calls - funded projects")
            plt.legend(handles, labels)
            plt.savefig("legal_type_coordination_all_calls.png", dpi=300)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments (both assigned before the first if statement)
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, [Participant role] role, Status FROM Annex7T7_new WHERE Status=='Main list' AND role == 'Coordinator' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY legal_type ORDER BY legal_type_count DESC"""
            data_coo = pd.read_sql(sql, conn)
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, [Participant role] role, Status FROM Annex7T7_new WHERE Status=='Main list' AND role LIKE 'Participant%' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY legal_type ORDER BY legal_type_count DESC"""
            data_part = pd.read_sql(sql, conn)
            colors = {'Coordinators':'tab:blue', 'Participants':'tab:orange'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(16,6))
            plt.bar(data_coo.legal_type, data_coo.legal_type_count, color='tab:blue',align='edge',width=-0.4)
            plt.bar(data_part.legal_type, data_part.legal_type_count, color='tab:orange',align='edge',width=0.4)
            plt.title("Participation by legal type: " + topic_name + year_name + " - funded projects")
            plt.legend(handles, labels)
            plt.savefig("legal_type_coordination_"+topic_name+year_name+".png", dpi=300)
            plt.close()

    elif group_type == "division_eu":
        if topic_name=="ALL":
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, division_eu, Status FROM Annex7T7_new WHERE Status=="Main list" AND division_eu="EU14" GROUP BY legal_type ORDER BY legal_type_count DESC"""
            eu14_legal = pd.read_sql(sql, conn)
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, division_eu, Status FROM Annex7T7_new WHERE Status=="Main list" AND division_eu="EU13" GROUP BY legal_type ORDER BY legal_type_count DESC"""
            eu13_legal = pd.read_sql(sql, conn)
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, division_eu, Status FROM Annex7T7_new WHERE Status=="Main list" AND division_eu="AC" GROUP BY legal_type ORDER BY legal_type_count DESC"""
            ac_legal = pd.read_sql(sql, conn)
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, division_eu, Status FROM Annex7T7_new WHERE Status=="Main list" AND division_eu="OTH" GROUP BY legal_type ORDER BY legal_type_count DESC"""
            oth_legal = pd.read_sql(sql, conn)
            colors = {'EU14':'tab:blue', 'EU13':'tab:orange', 'AC':'tab:green', 'OTH':'tab:grey'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(16,6))
            plt.xlim(-0.5,4.5)
            plt.bar(eu14_legal.legal_type.index-0.3, eu14_legal.legal_type_count,color=colors['EU14'],width=0.2)
            plt.bar(eu13_legal.legal_type.index-0.1, eu13_legal.legal_type_count,color=colors['EU13'],width=0.2)
            plt.bar(ac_legal.legal_type.index+0.1, ac_legal.legal_type_count,color=colors['AC'],width=0.2)
            plt.bar(oth_legal.legal_type.index+0.3, oth_legal.legal_type_count,color=colors['OTH'],width=0.2)
            plt.legend(handles, labels)
            plt.xticks(eu14_legal.legal_type.index, eu14_legal.legal_type.values)
            plt.title("Participation by legal type: all calls - per group - funded projects")
            plt.savefig("legal_type_groups_all_calls.png", dpi=300)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, division_eu, Status FROM Annex7T7_new WHERE Status=="Main list" AND division_eu="EU14" AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY legal_type ORDER BY legal_type_count DESC"""
            eu14_legal_topic = pd.read_sql(sql, conn)
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, division_eu, Status FROM Annex7T7_new WHERE Status=="Main list" AND division_eu="EU13" AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY legal_type ORDER BY legal_type_count DESC"""
            eu13_legal_topic = pd.read_sql(sql, conn)
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, division_eu, Status FROM Annex7T7_new WHERE Status=="Main list" AND division_eu="AC" AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY legal_type ORDER BY legal_type_count DESC"""
            ac_legal_topic = pd.read_sql(sql, conn)
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, division_eu, Status FROM Annex7T7_new WHERE Status=="Main list" AND division_eu="OTH" AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY legal_type ORDER BY legal_type_count DESC"""
            oth_legal_topic = pd.read_sql(sql, conn)
            colors = {'EU14':'tab:blue', 'EU13':'tab:orange', 'AC':'tab:green', 'OTH':'tab:grey'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.figure(figsize=(16,6))
            plt.xlim(-0.5,4.5)
            plt.bar(eu14_legal_topic.legal_type.index-0.3, eu14_legal_topic.legal_type_count,color=colors['EU14'],width=0.2)
            plt.bar(eu13_legal_topic.legal_type.index-0.1, eu13_legal_topic.legal_type_count,color=colors['EU13'],width=0.2)
            plt.bar(ac_legal_topic.legal_type.index+0.1, ac_legal_topic.legal_type_count,color=colors['AC'],width=0.2)
            plt.bar(oth_legal_topic.legal_type.index+0.3, oth_legal_topic.legal_type_count,color=colors['OTH'],width=0.2)
            plt.legend(handles, labels)
            plt.xticks(eu14_legal_topic.legal_type.index, eu14_legal_topic.legal_type.values)
            plt.title("Participation by legal type: " + topic_name + year_name + " - per group - funded projects")
            plt.savefig("legal_type_groups_"+topic_name+year_name+".png", dpi=300)
            plt.close()

    elif group_type=="widening":
        if topic_name=="ALL":
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, division_wd, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_wd=='WD' GROUP BY legal_type ORDER BY legal_type_count DESC"""
            data = pd.read_sql(sql, conn)
            plt.figure(figsize=(16,6))
            colors = {'WD':'tab:blue'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.bar(data.legal_type, data.legal_type_count,color=colors['WD'])
            plt.title("Participation by legal type: all calls - widening - funded projects")
            plt.legend(handles, labels)
            plt.savefig("legal_type_widening_all_calls.png", dpi=300)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, division_wd, Status FROM Annex7T7_new WHERE Status=='Main list' AND division_wd=='WD' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY legal_type ORDER BY legal_type_count DESC"""
            data = pd.read_sql(sql, conn)
            plt.figure(figsize=(16,6))
            colors = {'WD':'tab:blue'}
            labels = list(colors.keys())
            handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]  
            plt.bar(data.legal_type, data.legal_type_count,color=colors['WD'])
            plt.title("Participation by legal type: widening " + topic_name + year_name + " - funded projects")
            plt.legend(handles, labels)
            plt.savefig("legal_type_widening_"+topic_name+year_name+".png", dpi=300)
            plt.close()

    elif group_type=="pie":
        if topic_name=="ALL":
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, Status FROM Annex7T7_new WHERE Status="Main list" GROUP BY legal_type ORDER BY legal_type_count DESC"""
            main_list = pd.read_sql(sql, conn)
            labels = main_list.legal_type.values
            percentage = (main_list.legal_type_count/np.sum(main_list.legal_type_count)*100).values.tolist()
            sizes = [round(percentage) for percentage in percentage]
            explode = (0, 0, 0, 0, 0.2)  # only "explode" the n-th slice
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%.1f%%', rotatelabels=False, shadow=False, startangle=90, colors = mcolors.TABLEAU_COLORS)
            ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.title("Participations per legal type: All calls - funded projects")
            plt.savefig("legal_type_pie_all_calls.png", dpi=300)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments
            sql = """ SELECT count([Legal Type]) legal_type_count, [Legal Type] legal_type, Status FROM Annex7T7_new WHERE Status="Main list"  AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY legal_type  ORDER BY legal_type_count DESC"""
            main_list = pd.read_sql(sql, conn)
            labels = main_list.legal_type.values
            percentage = (main_list.legal_type_count/np.sum(main_list.legal_type_count)*100).values.tolist()
            sizes = [round(percentage) for percentage in percentage]
            explode = (0, 0, 0, 0, 0.2)  # only "explode" the n-th slice
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%.1f%%', rotatelabels=False, shadow=False, startangle=90, colors = mcolors.TABLEAU_COLORS)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.title('Participations per legal type: '+ topic_name + str(year_name) + " - funded projects")
            plt.savefig("legal_type_pie_"+ topic_name + str(year_name) + ".png", dpi=300)
            plt.close()

    else:
        # finally if none of the options is matched then error statement is printed.
        print("ERROR - you have selected group_type that is not supported by this function.")

### ------------ END OF FUNCTION LEGAL TYPE -----------------------------------




### ------------ FUNCTION COUNTRY GROUPS --------------------------------------
def country_groups(path_name,topic_name, year_name, group_type):
  
    # choose directory where the files and grpahs produced in this function will be stored
    folder_name = "country_groups"
    path_name = path_name + folder_name
    if not os.path.exists(path_name):
        os.mkdir(path_name)
    os.chdir(path_name)
    
    if group_type == "coordination_table":
        if topic_name=="ALL":
            # Division group count on the main list as participants
            sql = """ SELECT count(division_eu) count_division_eu , division_eu FROM Annex7T7_new WHERE Status="Main list" AND [Participant role]="Coordinator" GROUP BY division_eu ORDER BY count_division_eu DESC"""
            main_list_coo_eu = pd.read_sql(sql, conn)
            sql = """ SELECT count(division_eu) count_division_eu , division_eu FROM Annex7T7_new WHERE Status="Main list" AND [Participant role] LIKE "Participant%" GROUP BY division_eu ORDER BY count_division_eu DESC"""
            main_list_part_eu = pd.read_sql(sql, conn)
            
            [part14,part13,partac,partoth,coo14,coo13,cooac,coooth] = 8*[0]
            
            if main_list_coo_eu[main_list_coo_eu.division_eu=='EU14'].count_division_eu.empty == False: 
                coo14 = main_list_coo_eu[main_list_coo_eu.division_eu=='EU14'].count_division_eu.values[0]
            if main_list_coo_eu[main_list_coo_eu.division_eu=='EU13'].count_division_eu.empty == False: 
                coo13 = main_list_coo_eu[main_list_coo_eu.division_eu=='EU13'].count_division_eu.values[0]
            if main_list_coo_eu[main_list_coo_eu.division_eu=='AC'].count_division_eu.empty == False: 
                cooac = main_list_coo_eu[main_list_coo_eu.division_eu=='AC'].count_division_eu.values[0]
            if main_list_coo_eu[main_list_coo_eu.division_eu=='OTH'].count_division_eu.empty == False: 
                coooth = main_list_coo_eu[main_list_coo_eu.division_eu=='OTH'].count_division_eu.values[0]
                
            if main_list_part_eu[main_list_part_eu.division_eu=='EU14'].count_division_eu.empty == False: 
                part14 = main_list_part_eu[main_list_part_eu.division_eu=='EU14'].count_division_eu.values[0]
            if main_list_part_eu[main_list_part_eu.division_eu=='EU13'].count_division_eu.empty == False: 
                part13 = main_list_part_eu[main_list_part_eu.division_eu=='EU13'].count_division_eu.values[0]
            if main_list_part_eu[main_list_part_eu.division_eu=='AC'].count_division_eu.empty == False: 
                partac = main_list_part_eu[main_list_part_eu.division_eu=='AC'].count_division_eu.values[0]
            if main_list_part_eu[main_list_part_eu.division_eu=='OTH'].count_division_eu.empty == False: 
                partoth = main_list_part_eu[main_list_part_eu.division_eu=='OTH'].count_division_eu.values[0]
            
            country_type = ('EU-14','EU-13','AC','OTH')
            width = 0.4 
            x = np.arange(len(country_type))  # label locations
            ax_left, ax_bottom, ax_width, ax_height = 0.1, 0.3, 0.8, 0.65  # Axes location
            plt.figure(figsize=(12,5))
            ax = plt.axes([ax_left, ax_bottom, ax_width, ax_height])
            # dataset in next line must be arranged same as country type, otherwise the numbers and x axes text will not correspond
            dataset =  [[coo14,coo13,cooac,coooth],[part14,part13,partac,partoth]]
            rects1 = ax.bar(x - width/2, [coo14,coo13,cooac,coooth], width, label='Coordinators', color='tab:blue')
            rects2 = ax.bar(x + width/2, [part14,part13,partac,partoth], width, label='Participants', color='tab:orange')
            # Add some text for labels, title and custom x-axis tick labels, etc.
            ax.set_xticks(x, country_type)
            ymin,ymax = ax.get_ylim()
            ax.set_ylim([ymin,ymax+(0.05*ymax)]) #limit for ymax must be little bit higher because we need to add the percentage on top of bar
            ax.set_xlim(-0.5, len(dataset[0]) - 0.5)
            ax.legend()
            plt.title('Country group participation count: all calls - funded projects')
            
            # rects= ax.patches
            labels = np.round(np.array([coo14,coo13,cooac,coooth])/sum([coo14,coo13,cooac,coooth]) * 100.,1)
            #labels = [cooac,coo13,coo27,coonone]
            for rect, label in zip(rects1.patches, labels):
                height = rect.get_height()
                if (label > 0):
                    ax.text(
                        rect.get_x() + rect.get_width()/2, height + 1, str(label)+'%', ha="center", va="bottom"
                        )
            labels = np.round(np.array([part14,part13,partac,partoth])/sum([part14,part13,partac,partoth]) * 100.,1)
            for rect, label in zip(rects2.patches, labels):
                height = rect.get_height()
                if (label > 0):
                    ax.text(
                        rect.get_x() + rect.get_width() / 2, height + 1, str(label)+'%', ha="center", va="bottom"
                        )
            rcolors = ['tab:blue','tab:orange']
            columns = ('EU-14','EU-13','AC','OTH')
            rows = ['Coordinators','Participants']
            mtable.table(ax, cellText=dataset, rowColours=rcolors, rowLabels=rows, colLabels=columns, cellLoc="center", bbox=(0, -ax_bottom / ax_height, 1, ax_bottom / ax_height))
            plt.xticks([])
            plt.savefig("country_group_table_all_calls.png",dpi=300)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments (both assigned before the first if statement)
            sql = """ SELECT count(division_eu) count_division_eu , division_eu FROM Annex7T7_new WHERE Status="Main list" AND [Participant role]="Coordinator" AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY division_eu ORDER BY count_division_eu DESC"""
            main_list_coo_eu = pd.read_sql(sql, conn)
            sql = """ SELECT count(division_eu) count_division_eu , division_eu FROM Annex7T7_new WHERE Status="Main list" AND [Participant role] LIKE "Participant%" AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" GROUP BY division_eu ORDER BY count_division_eu DESC"""
            main_list_part_eu = pd.read_sql(sql, conn)
            
            [part14,part13,partac,partoth,coo14,coo13,cooac,coooth] = 8*[0]
            
            if main_list_coo_eu[main_list_coo_eu.division_eu=='EU14'].count_division_eu.empty == False: 
                coo14 = main_list_coo_eu[main_list_coo_eu.division_eu=='EU14'].count_division_eu.values[0]
            if main_list_coo_eu[main_list_coo_eu.division_eu=='EU13'].count_division_eu.empty == False: 
                coo13 = main_list_coo_eu[main_list_coo_eu.division_eu=='EU13'].count_division_eu.values[0]
            if main_list_coo_eu[main_list_coo_eu.division_eu=='AC'].count_division_eu.empty == False: 
                cooac = main_list_coo_eu[main_list_coo_eu.division_eu=='AC'].count_division_eu.values[0]
            if main_list_coo_eu[main_list_coo_eu.division_eu=='OTH'].count_division_eu.empty == False: 
                coooth = main_list_coo_eu[main_list_coo_eu.division_eu=='OTH'].count_division_eu.values[0]
                
            if main_list_part_eu[main_list_part_eu.division_eu=='EU14'].count_division_eu.empty == False: 
                part14 = main_list_part_eu[main_list_part_eu.division_eu=='EU14'].count_division_eu.values[0]
            if main_list_part_eu[main_list_part_eu.division_eu=='EU13'].count_division_eu.empty == False: 
                part13 = main_list_part_eu[main_list_part_eu.division_eu=='EU13'].count_division_eu.values[0]
            if main_list_part_eu[main_list_part_eu.division_eu=='AC'].count_division_eu.empty == False: 
                partac = main_list_part_eu[main_list_part_eu.division_eu=='AC'].count_division_eu.values[0]
            if main_list_part_eu[main_list_part_eu.division_eu=='OTH'].count_division_eu.empty == False: 
                partoth = main_list_part_eu[main_list_part_eu.division_eu=='OTH'].count_division_eu.values[0]
            
            country_type = ('EU-14','EU-13','AC','OTH')
            width = 0.4 
            x = np.arange(len(country_type))  # label locations
            ax_left, ax_bottom, ax_width, ax_height = 0.1, 0.3, 0.8, 0.65  # Axes location
            plt.figure(figsize=(12,5))
            ax = plt.axes([ax_left, ax_bottom, ax_width, ax_height])
            # dataset in next line must be arranged same as country type, otherwise the numbers and x axes text will not correspond
            dataset =  [[coo14,coo13,cooac,coooth],[part14,part13,partac,partoth]]
            rects1 = ax.bar(x - width/2, [coo14,coo13,cooac,coooth], width, label='Coordinators', color='tab:blue')
            rects2 = ax.bar(x + width/2, [part14,part13,partac,partoth], width, label='Participants', color='tab:orange')
            # Add some text for labels, title and custom x-axis tick labels, etc.
            ax.set_xticks(x, country_type)
            ymin,ymax = ax.get_ylim()
            ax.set_ylim([ymin,ymax+(0.05*ymax)]) #limit for ymax must be little bit higher because we need to add the percentage on top of bar
            ax.set_xlim(-0.5, len(dataset[0]) - 0.5)
            ax.legend()
            plt.title("Country group participation count: " + topic_name + str(year_name) +  "- funded projects")
            
            # rects= ax.patches
            labels = np.round(np.array([coo14,coo13,cooac,coooth])/sum([coo14,coo13,cooac,coooth]) * 100.,1)
            #labels = [cooac,coo13,coo27,coonone]
            for rect, label in zip(rects1.patches, labels):
                height = rect.get_height()
                if (label > 0):
                    ax.text(
                        rect.get_x() + rect.get_width()/2, height + 1, str(label)+'%', ha="center", va="bottom"
                        )
            labels = np.round(np.array([part14,part13,partac,partoth])/sum([part14,part13,partac,partoth]) * 100.,1)
            for rect, label in zip(rects2.patches, labels):
                height = rect.get_height()
                if (label > 0):
                    ax.text(
                        rect.get_x() + rect.get_width() / 2, height + 1, str(label)+'%', ha="center", va="bottom"
                        )
            rcolors = ['tab:blue','tab:orange']
            columns = ('EU-14','EU-13','AC','OTH')
            rows = ['Coordinators','Participants']
            mtable.table(ax, cellText=dataset, rowColours=rcolors, rowLabels=rows, colLabels=columns, cellLoc="center", bbox=(0, -ax_bottom / ax_height, 1, ax_bottom / ax_height))
            plt.xticks([])
            plt.savefig("country_group_table_" + topic_name + str(year_name) + ".png", dpi=300)            
            plt.close()

    elif group_type == "type_of_action":
        if topic_name=="ALL":
            sql_ria = """ SELECT division_eu FROM Annex7T7_new WHERE Status="Main list" AND [Type of Action] == 'HORIZON-RIA' """
            sql_ia = """ SELECT division_eu FROM Annex7T7_new WHERE Status="Main list" AND [Type of Action] == 'HORIZON-IA' """
            sql_csa = """ SELECT division_eu FROM Annex7T7_new WHERE Status="Main list" AND [Type of Action] == 'HORIZON-CSA' """
            ria = pd.read_sql(sql_ria, conn)
            ia = pd.read_sql(sql_ia, conn)
            csa = pd.read_sql(sql_csa, conn)
            eu14_list = np.array( [len(ria[ria.division_eu == 'EU14'].division_eu), len(ia[ia.division_eu == 'EU14'].division_eu), len(csa[csa.division_eu == 'EU14'].division_eu) ])
            sizes_eu14 = np.round(np.array(eu14_list/eu14_list.sum()) * 100.,1)
            eu13_list = np.array( [len(ria[ria.division_eu == 'EU13'].division_eu), len(ia[ia.division_eu == 'EU13'].division_eu), len(csa[csa.division_eu == 'EU13'].division_eu) ])
            sizes_eu13 = np.round(np.array(eu13_list/eu13_list.sum()) * 100.,1)
            ac_list = np.array( [len(ria[ria.division_eu == 'AC'].division_eu), len(ia[ia.division_eu == 'AC'].division_eu), len(csa[csa.division_eu == 'AC'].division_eu) ])
            sizes_ac = np.round(np.array(ac_list/ac_list.sum()) * 100.,1)
            oth_list = np.array( [len(ria[ria.division_eu == 'OTH'].division_eu), len(ia[ia.division_eu == 'OTH'].division_eu), len(csa[csa.division_eu == 'OTH'].division_eu) ])
            sizes_oth = np.round(np.array(oth_list/oth_list.sum()) * 100.,1)
            fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(10,3))
            # first is example where explode function is used, and second one without it
            ax1.pie(sizes_eu14[(sizes_eu14 != 0)], explode=(0,0,0.1), autopct=lambda p: '{:1.1f}%'.format(p) if p > 0 else None, shadow=False, startangle=90, labels=[['RIA','IA','CSA'][x] for x in [i for i, x in enumerate((sizes_eu14 != 0)) if x]])
            # ax1.pie(sizes_eu14[(sizes_eu14 != 0)], autopct=lambda p: '{:1.1f}%'.format(p) if p > 0 else None, shadow=False, startangle=90, labels=[['RIA','IA','CSA'][x] for x in [i for i, x in enumerate((sizes_eu14 != 0)) if x]], colors = mcolors.TABLEAU_COLORS)
            ax2.pie(sizes_eu13[(sizes_eu13 != 0)], autopct=lambda p: '{:1.1f}%'.format(p) if p > 0 else None, shadow=False, startangle=90, labels=[['RIA','IA','CSA'][x] for x in [i for i, x in enumerate((sizes_eu13 != 0)) if x]], colors = mcolors.TABLEAU_COLORS)
            ax3.pie(sizes_ac[(sizes_ac != 0)], autopct=lambda p: '{:1.1f}%'.format(p) if p > 0 else None, shadow=False, startangle=90, labels=[['RIA','IA','CSA'][x] for x in [i for i, x in enumerate((sizes_ac != 0)) if x]], colors = mcolors.TABLEAU_COLORS)
            ax4.pie(sizes_oth[(sizes_oth != 0)], explode=(0,0,0.1), autopct=lambda p: '{:1.1f}%'.format(p) if p > 0 else None, shadow=False, startangle=90, labels=[['RIA','IA','CSA'][x] for x in [i for i, x in enumerate((sizes_oth != 0)) if x]], colors = mcolors.TABLEAU_COLORS)
            ax1.axis('equal')
            ax1.set_title('EU-14')
            ax2.axis('equal')
            ax2.set_title('EU-13')
            ax3.axis('equal')
            ax3.set_title('AC')
            ax4.axis('equal')
            ax4.set_title('OTH')
            plt.suptitle("Country group type of action: all calls - funded projects")
            plt.tight_layout()
            plt.savefig("country_group_type_of_action_all_calls.png", dpi=300)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments
            sql_ria = """ SELECT division_eu FROM Annex7T7_new WHERE Status="Main list" AND [Type of Action] == 'HORIZON-RIA' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" """
            sql_ia = """ SELECT division_eu FROM Annex7T7_new WHERE Status="Main list" AND [Type of Action] == 'HORIZON-IA' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" """
            sql_csa = """ SELECT division_eu FROM Annex7T7_new WHERE Status="Main list" AND [Type of Action] == 'HORIZON-CSA' AND Topic LIKE """+ '"'+ topic_name + str(year_name)+"""-SPACE%" """
            ria = pd.read_sql(sql_ria, conn)
            ia = pd.read_sql(sql_ia, conn)
            csa = pd.read_sql(sql_csa, conn)
            eu14_list = np.array( [len(ria[ria.division_eu == 'EU14'].division_eu), len(ia[ia.division_eu == 'EU14'].division_eu), len(csa[csa.division_eu == 'EU14'].division_eu) ])
            sizes_eu14 = np.round(np.array(eu14_list/eu14_list.sum()) * 100.,1)
            eu13_list = np.array( [len(ria[ria.division_eu == 'EU13'].division_eu), len(ia[ia.division_eu == 'EU13'].division_eu), len(csa[csa.division_eu == 'EU13'].division_eu) ])
            sizes_eu13 = np.round(np.array(eu13_list/eu13_list.sum()) * 100.,1)
            ac_list = np.array( [len(ria[ria.division_eu == 'AC'].division_eu), len(ia[ia.division_eu == 'AC'].division_eu), len(csa[csa.division_eu == 'AC'].division_eu) ])
            sizes_ac = np.round(np.array(ac_list/ac_list.sum()) * 100.,1)
            oth_list = np.array( [len(ria[ria.division_eu == 'OTH'].division_eu), len(ia[ia.division_eu == 'OTH'].division_eu), len(csa[csa.division_eu == 'OTH'].division_eu) ])
            sizes_oth = np.round(np.array(oth_list/oth_list.sum()) * 100.,1)
            fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(10,3))
            # first is example where explode function is used, and second one without it
            # ax1.pie(sizes_eu14[(sizes_eu14 != 0)], explode=(0,0,0.1), autopct=lambda p: '{:1.1f}%'.format(p) if p > 0 else None, shadow=False, startangle=90, labels=[['RIA','IA','CSA'][x] for x in [i for i, x in enumerate((sizes_eu14 != 0)) if x]])
            ax1.pie(sizes_eu14[(sizes_eu14 != 0)], autopct=lambda p: '{:1.1f}%'.format(p) if p > 0 else None, shadow=False, startangle=90, labels=[['RIA','IA','CSA'][x] for x in [i for i, x in enumerate((sizes_eu14 != 0)) if x]], colors = mcolors.TABLEAU_COLORS)
            ax2.pie(sizes_eu13[(sizes_eu13 != 0)], autopct=lambda p: '{:1.1f}%'.format(p) if p > 0 else None, shadow=False, startangle=90, labels=[['RIA','IA','CSA'][x] for x in [i for i, x in enumerate((sizes_eu13 != 0)) if x]], colors = mcolors.TABLEAU_COLORS)
            ax3.pie(sizes_ac[(sizes_ac != 0)], autopct=lambda p: '{:1.1f}%'.format(p) if p > 0 else None, shadow=False, startangle=90, labels=[['RIA','IA','CSA'][x] for x in [i for i, x in enumerate((sizes_ac != 0)) if x]], colors = mcolors.TABLEAU_COLORS)
            ax4.pie(sizes_oth[(sizes_oth != 0)], autopct=lambda p: '{:1.1f}%'.format(p) if p > 0 else None, shadow=False, startangle=90, labels=[['RIA','IA','CSA'][x] for x in [i for i, x in enumerate((sizes_oth != 0)) if x]], colors = mcolors.TABLEAU_COLORS)
            ax1.axis('equal')
            ax1.set_title('EU-14')
            ax2.axis('equal')
            ax2.set_title('EU-13')
            ax3.axis('equal')
            ax3.set_title('AC')
            ax4.axis('equal')
            ax4.set_title('OTH')
            plt.suptitle("Country group type of action: " + topic_name + str(year_name) + " - funded projects")
            plt.tight_layout()
            plt.savefig("country_group_type_of_action_" + topic_name + str(year_name) + ".png", dpi=300)
            plt.close()

    else:
        # finally if none of the options is matched then error statement is printed.
        print("ERROR - you have selected group_type that is not supported by this function.")

### ------------ END OF FUNCTION COUNTRY GROUPS -------------------------------




### ----------- FUNCTION SUCCESS RATE  -----------------------------------------
def success_rate(path_name,topic_name, year_name, group_type):
    
    # choose directory where the files and grpahs produced in this function will be stored
    folder_name = "success_rate"
    path_name = path_name + folder_name
    if not os.path.exists(path_name):
        os.mkdir(path_name)
    os.chdir(path_name)
    x_axis_file = open('x_axis_file.txt', mode='a+')

    if group_type == "groups_with_avg":
        if topic_name=="ALL":
            # queries for participants and coordinators for ALL calls and years
            sql_main = """ SELECT * FROM Annex7T7_new WHERE Status="Main list" """
            list_main = pd.read_sql(sql_main,conn)
            # when looking for the total number of participation for some contry, we just dont take ineligible calls, everything else goes to sum.
            sql_all = """ SELECT * FROM Annex7T7_new WHERE Status!="Ineligible" """
            list_all = pd.read_sql(sql_all,conn)
            # first we calculate average for EU27 and then we add that value to avg. In case we want to change to average EU14 include different line, and then add that value to avg.
            avg_eu27 = list_main[list_main.division_eu27=='EU27'].Country.value_counts().values.sum()/list_all[list_all.division_eu27=='EU27'].Country.value_counts().values.sum() * 100.
            avg = avg_eu27
            # we create 3 lists, 2 are empty for now
            country_name  = list_main.Country.value_counts().index.values.tolist()
            country_score = []
            division = []
            for x in country_name:
                ## to calculate sr (success rate) we need number of participation on main divided by all participation for each country.
                country_on_main = list_main.Country.value_counts()[list_main.Country.value_counts().index==x].values
                country_on_all = list_all.Country.value_counts()[list_all.Country.value_counts().index==x].values
                ## success rate is:
                sr = (country_on_main / country_on_all * 100.0)[0] ## sr is list so we need just first element that is why we use [0]
                country_score.append(sr)
                ## now with the list of country scores we need another list same length, with exactly which division that country is assigned.
                division.append(list_main[list_main.Country.values == x].division_eu.values[0])
            ## finaly we create a data frame score_df with 3 values in order to sort that and then plot.
            score_df = pd.DataFrame({"Name" : country_name, "Score" : country_score, "Division" : division})
            score_df = score_df.sort_values(by=['Score'],ascending=False)
            plt.figure(figsize=(14,6))
            #we plot bars with values from score_df Name and Score, acording to the group.
            plt.bar(score_df.Name[score_df.Division=='EU14'], score_df.Score[score_df.Division=='EU14'], color='tab:blue',label='EU14') 
            plt.bar(score_df.Name[score_df.Division=='EU13'], score_df.Score[score_df.Division=='EU13'], color='tab:orange',label='EU13') 
            plt.bar(score_df.Name[score_df.Division=='AC'], score_df.Score[score_df.Division=='AC'], color='tab:green',label='AC') 
            plt.bar(score_df.Name[score_df.Division=='OTH'], score_df.Score[score_df.Division=='OTH'], color='grey',label='OTH') 
            plt.xticks(rotation=45)
            # now we calculate and plot horizontal lines for average avlue, 70% of average value and 120% of average value.
            plt.hlines(1.2*avg, xmin=0, xmax=len(score_df), color='black', ls='dashed')
            plt.text(0.3*len(score_df), 1.25*avg, str('120% average' ) , color='black', fontsize=12, fontweight=600)
            plt.hlines(avg, xmin=0, xmax=len(score_df), color='black')
            plt.text(0.3*len(score_df), 1.05*avg, 'EU27 average = '+ str(np.round(avg, decimals=2)) + '%', color='black', fontsize=12, fontweight=600)
            plt.hlines(0.7*avg, xmin=0, xmax=len(score_df), color='black', ls='dotted')
            plt.text(0.3*len(score_df), 0.75*avg, str('70% average') , color='black', fontsize=12, fontweight=600)
            plt.legend()
            plt.title("Country success rate: all calls - per group")
            name_graph="country_success_rate_all_calls.png"
            plt.savefig(name_graph, bbox_inches='tight', dpi=300)
            plt.savefig(name_graph, dpi=300)
            first_axis=score_df.Name[score_df.Division=='EU14'].to_string(index=False).split("\n")
            second_axis=score_df.Name[score_df.Division=='EU13'].to_string(index=False).split("\n")
            third_axis=score_df.Name[score_df.Division=='AC'].to_string(index=False).split("\n")
            fourth_axis=score_df.Name[score_df.Division=='OTH'].to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis + third_axis + fourth_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments
            sql_main = """ SELECT * FROM Annex7T7_new WHERE Status="Main list" AND Topic LIKE """+ '"'+ topic_name + str(year_name) + """-SPACE%" """
            list_main = pd.read_sql(sql_main,conn)
            sql_all = """ SELECT * FROM Annex7T7_new WHERE Status!="Ineligible" AND Topic LIKE """+ '"'+ topic_name + str(year_name) + """-SPACE%" """
            list_all = pd.read_sql(sql_all,conn)
            # first we calculate average for EU27 and then we add that value to avg. In case we want to change to average EU14 include different line, and then add that value to avg.
            avg_eu27 = list_main[list_main.division_eu27=='EU27'].Country.value_counts().values.sum()/list_all[list_all.division_eu27=='EU27'].Country.value_counts().values.sum() * 100.
            avg = avg_eu27
            # we create 3 lists, 2 are empty for now
            country_name  = list_main.Country.value_counts().index.values.tolist()
            country_score = []
            division = []
            for x in country_name:
                ## to calculate sr (success rate) we need number of participation on main divided by all participation for each country.
                country_on_main = list_main.Country.value_counts()[list_main.Country.value_counts().index==x].values
                country_on_all = list_all.Country.value_counts()[list_all.Country.value_counts().index==x].values
                ## success rate is:
                sr = (country_on_main / country_on_all * 100.0)[0] ## sr is list so we need just first element that is why we use [0]
                country_score.append(sr)
                ## now with the list of country scores we need another list same length, with exactly which division that country is assigned.
                division.append(list_main[list_main.Country.values == x].division_eu.values[0])
            ## finaly we create a data frame score_df with 3 values in order to sort that and then plot.
            score_df = pd.DataFrame({"Name" : country_name, "Score" : country_score, "Division" : division})
            score_df = score_df.sort_values(by=['Score'],ascending=False)
            plt.figure(figsize=(14,6))
            #we plot bars with values from score_df Name and Score, acording to the group.
            plt.bar(score_df.Name[score_df.Division=='EU14'], score_df.Score[score_df.Division=='EU14'], color='tab:blue',label='EU14') 
            plt.bar(score_df.Name[score_df.Division=='EU13'], score_df.Score[score_df.Division=='EU13'], color='tab:orange',label='EU13') 
            plt.bar(score_df.Name[score_df.Division=='AC'], score_df.Score[score_df.Division=='AC'], color='tab:green',label='AC') 
            plt.bar(score_df.Name[score_df.Division=='OTH'], score_df.Score[score_df.Division=='OTH'], color='grey',label='OTH') 
            # plt.xticks(rotation=90)
            # now we calculate and plot horizontal lines for average avlue, 70% of average value and 120% of average value.
            plt.hlines(1.2*avg, xmin=0, xmax=len(score_df), color='black', ls='dashed')
            plt.text(0.3*len(score_df), 1.25*avg, str('120% average' ) , color='black', fontsize=12, fontweight=600)
            plt.hlines(avg, xmin=0, xmax=len(score_df), color='black')
            plt.text(0.3*len(score_df), 1.05*avg, 'EU27 average = '+ str(np.round(avg, decimals=2)) + '%', color='black', fontsize=12, fontweight=600)
            plt.hlines(0.7*avg, xmin=0, xmax=len(score_df), color='black', ls='dotted')
            plt.text(0.3*len(score_df), 0.75*avg, str('70% average') , color='black', fontsize=12, fontweight=600)
            plt.legend()
            plt.title("Country success rate: " + topic_name + str(year_name) + " - per group")
            name_graph="country_success_rate_" + topic_name + str(year_name) + ".png"
            plt.savefig(name_graph, bbox_inches='tight', dpi=300)
            first_axis=score_df.Name[score_df.Division=='EU14'].to_string(index=False).split("\n")
            second_axis=score_df.Name[score_df.Division=='EU13'].to_string(index=False).split("\n")
            third_axis=score_df.Name[score_df.Division=='AC'].to_string(index=False).split("\n")
            fourth_axis=score_df.Name[score_df.Division=='OTH'].to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis + third_axis + fourth_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

    elif group_type == "groups_with_avg_number_proposals":
        if topic_name=="ALL":
            sql_main = """ SELECT * FROM Annex7T7_new WHERE Status="Main list" """
            list_main = pd.read_sql(sql_main,conn)
            # when looking for the total number of participation for some contry, we just dont take ineligible calls, everything else goes to sum.
            sql_all = """ SELECT * FROM Annex7T7_new WHERE Status!="Ineligible" """
            list_all = pd.read_sql(sql_all,conn)
            # we create 3 lists, 2 are empty for now
            country_name  = list_main.Country.value_counts().index.values.tolist()
            country_score = []
            country_on_main = []
            country_on_all = []
            division = []
            for x in country_name:
                ## to calculate sr (success rate) we need number of participation on main divided by all participation for each country.
                c_main = list_main.Country.value_counts()[list_main.Country.value_counts().index==x].values
                c_all = list_all.Country.value_counts()[list_all.Country.value_counts().index==x].values
                ## success rate is:
                sr = (c_main / c_all * 100.0)[0] ## sr is list so we need just first element that is why we use [0]
                country_score.append(sr)
                country_on_main.append(c_main[0])
                country_on_all.append(c_all[0])
                ## now with the list of country scores we need another list same length, with exactly which division that country is assigned.
                division.append(list_main[list_main.Country.values == x].division_eu.values[0])
            ## finaly we create a data frame score_df with 3 values in order to sort that and then plot.
            score_df = pd.DataFrame({"Name" : country_name, "Score" : country_score, "Division" : division,
                                     "Funded" : country_on_main, "Proposed" : country_on_all})
            score_df = score_df.sort_values(by=['Score'],ascending=False)
            ### za anu, zasto ovde nemamo Division=='OTH' kao u prethodnim slucajevima (search for that)
            fig = plt.figure(figsize=(14,6))
            #we plot bars with values from score_df Name and Score, acording to the group.
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.bar(score_df.Name[score_df.Division=='EU14'], score_df.Funded[score_df.Division=='EU14'], color='tab:blue',label='EU14 funded',align='edge',width=-0.4) 
            ax1.bar(score_df.Name[score_df.Division=='EU14'], score_df.Proposed[score_df.Division=='EU14'], color='tab:cyan',align='edge',width=0.4)
            ax2.scatter(score_df.Name[score_df.Division=='EU14'], score_df.Score[score_df.Division=='EU14'], c='tab:brown')
            ax1.bar(score_df.Name[score_df.Division=='EU13'], score_df.Funded[score_df.Division=='EU13'], color='tab:orange',label='EU13 funded',align='edge',width=-0.4) 
            ax1.bar(score_df.Name[score_df.Division=='EU13'], score_df.Proposed[score_df.Division=='EU13'], color='tab:cyan',align='edge',width=0.4)
            ax2.scatter(score_df.Name[score_df.Division=='EU13'], score_df.Score[score_df.Division=='EU13'], c='tab:brown')
            ax1.bar(score_df.Name[score_df.Division=='AC'], score_df.Funded[score_df.Division=='AC'], color='tab:green',label='AC funded',align='edge',width=-0.4) 
            ax1.bar(score_df.Name[score_df.Division=='AC'], score_df.Proposed[score_df.Division=='AC'], color='tab:cyan',label='Proposed',align='edge',width=0.4)
            ax2.scatter(score_df.Name[score_df.Division=='AC'], score_df.Score[score_df.Division=='AC'], c='tab:brown',label='Succes rate')
            # adding all names and scores as percentage to list and then to annotate function that is connected with scatter plot
            nam14 = score_df.Name[score_df.Division=='EU14'].values.tolist()
            nam13 = score_df.Name[score_df.Division=='EU13'].values.tolist()
            namac = score_df.Name[score_df.Division=='AC'].values.tolist()
            nam = nam14 + nam13 + namac
            sco = score_df.Score[score_df.Division=='EU14'].values.tolist() + score_df.Score[score_df.Division=='EU13'].values.tolist() + score_df.Score[score_df.Division=='AC'].values.tolist()
            for i, txt in enumerate(sco):
                ax2.annotate(np.round(sco[i],decimals=1), (nam[i],sco[i]+2), ha="center")
            # Now we calculate averages to add them to graph, and we also use nam14, nam13, namac
            avg_eu27 = list_main[list_main.division_eu27=='EU27'].Country.value_counts().values.sum()/list_all[list_all.division_eu27=='EU27'].Country.value_counts().values.sum() * 100.
            avg_eu14 = list_main[list_main.division_eu=='EU14'].Country.value_counts().values.sum()/list_all[list_all.division_eu=='EU14'].Country.value_counts().values.sum() * 100.
            avg_eu13 = list_main[list_main.division_eu=='EU13'].Country.value_counts().values.sum()/list_all[list_all.division_eu=='EU13'].Country.value_counts().values.sum() * 100.
            avg_ac = list_main[list_main.division_eu=='AC'].Country.value_counts().values.sum()/list_all[list_all.division_eu=='AC'].Country.value_counts().values.sum() * 100.
            len_eu14 = len(nam14)
            len_eu13 = len(nam13)
            len_ac = len(namac)
            plt.hlines(avg_eu14, xmin=0, xmax=len_eu14-1, color='tab:blue', ls='dashed', label="EU14 average")
            plt.hlines(avg_eu13, xmin=len_eu14, xmax=len_eu14+len_eu13-1, color='tab:orange', ls='dashed', label="EU13 average")
            plt.hlines(avg_ac, xmin=len_eu14+len_eu13, xmax=len_eu14+len_eu13+len_ac-1, color='tab:green', ls='dashed', label="AC average")
            handles, labels = ax1.get_legend_handles_labels()
            handles2, labels2 = ax2.get_legend_handles_labels()
            ax2.legend(handles + handles2, labels + labels2, loc=0)
            # plt.xticks(rotation=90)
            fig.tight_layout() 
            plt.title("Country success rate with number of proposals: all calls - per group")
            name_graph="country_success_rate_number_proposals_all_calls.png"
            plt.savefig(name_graph, bbox_inches='tight', dpi=300)
            first_axis=score_df.Name[score_df.Division=='EU14'].to_string(index=False).split("\n")
            second_axis=score_df.Name[score_df.Division=='EU13'].to_string(index=False).split("\n")
            third_axis=score_df.Name[score_df.Division=='AC'].to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis + third_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

        else:
            # use topic_name and year_name from the function arguments
            sql_main = """ SELECT * FROM Annex7T7_new WHERE Status="Main list" AND Topic LIKE """+ '"'+ topic_name + str(year_name) + """-SPACE%" """
            list_main = pd.read_sql(sql_main,conn)
            # when looking for the total number of participation for some contry, we just dont take ineligible calls, everything else goes to sum.
            sql_all = """ SELECT * FROM Annex7T7_new WHERE Status!="Ineligible" AND Topic LIKE """+ '"'+ topic_name + str(year_name) + """-SPACE%" """
            list_all = pd.read_sql(sql_all,conn)
            # we create 3 lists, 2 are empty for now
            country_name  = list_main.Country.value_counts().index.values.tolist()
            country_score = []
            country_on_main = []
            country_on_all = []
            division = []
            for x in country_name:
                ## to calculate sr (success rate) we need number of participation on main divided by all participation for each country.
                c_main = list_main.Country.value_counts()[list_main.Country.value_counts().index==x].values
                c_all = list_all.Country.value_counts()[list_all.Country.value_counts().index==x].values
                ## success rate is:
                sr = (c_main / c_all * 100.0)[0] ## sr is list so we need just first element that is why we use [0]
                country_score.append(sr)
                country_on_main.append(c_main[0])
                country_on_all.append(c_all[0])
                ## now with the list of country scores we need another list same length, with exactly which division that country is assigned.
                division.append(list_main[list_main.Country.values == x].division_eu.values[0])
            ## finaly we create a data frame score_df with 3 values in order to sort that and then plot.
            score_df = pd.DataFrame({"Name" : country_name, "Score" : country_score, "Division" : division,
                                     "Funded" : country_on_main, "Proposed" : country_on_all})
            score_df = score_df.sort_values(by=['Score'],ascending=False)
            
            fig = plt.figure(figsize=(14,6))
            #we plot bars with values from score_df Name and Score, acording to the group.
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.bar(score_df.Name[score_df.Division=='EU14'], score_df.Funded[score_df.Division=='EU14'], color='tab:blue',label='EU14 funded',align='edge',width=-0.4) 
            ax1.bar(score_df.Name[score_df.Division=='EU14'], score_df.Proposed[score_df.Division=='EU14'], color='tab:cyan',align='edge',width=0.4)
            ax2.scatter(score_df.Name[score_df.Division=='EU14'], score_df.Score[score_df.Division=='EU14'], c='tab:brown')
            ax1.bar(score_df.Name[score_df.Division=='EU13'], score_df.Funded[score_df.Division=='EU13'], color='tab:orange',label='EU13 funded',align='edge',width=-0.4) 
            ax1.bar(score_df.Name[score_df.Division=='EU13'], score_df.Proposed[score_df.Division=='EU13'], color='tab:cyan',align='edge',width=0.4)
            ax2.scatter(score_df.Name[score_df.Division=='EU13'], score_df.Score[score_df.Division=='EU13'], c='tab:brown')
            ax1.bar(score_df.Name[score_df.Division=='AC'], score_df.Funded[score_df.Division=='AC'], color='tab:green',label='AC funded',align='edge',width=-0.4) 
            ax1.bar(score_df.Name[score_df.Division=='AC'], score_df.Proposed[score_df.Division=='AC'], color='tab:cyan',label='Proposed',align='edge',width=0.4)
            ax2.scatter(score_df.Name[score_df.Division=='AC'], score_df.Score[score_df.Division=='AC'], c='tab:brown',label='Succes rate')
            # adding all names and scores as percentage to list and then to annotate function that is connected with scatter plot
            nam14 = score_df.Name[score_df.Division=='EU14'].values.tolist()
            nam13 = score_df.Name[score_df.Division=='EU13'].values.tolist()
            namac = score_df.Name[score_df.Division=='AC'].values.tolist()
            nam = nam14 + nam13 + namac
            sco = score_df.Score[score_df.Division=='EU14'].values.tolist() + score_df.Score[score_df.Division=='EU13'].values.tolist() + score_df.Score[score_df.Division=='AC'].values.tolist()
            for i, txt in enumerate(sco):
                ax2.annotate(np.round(sco[i],decimals=1), (nam[i],sco[i]+2), ha="center")
            # Now we calculate averages to add them to graph, and we also use nam14, nam13, namac
            avg_eu27 = list_main[list_main.division_eu27=='EU27'].Country.value_counts().values.sum()/list_all[list_all.division_eu27=='EU27'].Country.value_counts().values.sum() * 100.
            avg_eu14 = list_main[list_main.division_eu=='EU14'].Country.value_counts().values.sum()/list_all[list_all.division_eu=='EU14'].Country.value_counts().values.sum() * 100.
            avg_eu13 = list_main[list_main.division_eu=='EU13'].Country.value_counts().values.sum()/list_all[list_all.division_eu=='EU13'].Country.value_counts().values.sum() * 100.
            avg_ac = list_main[list_main.division_eu=='AC'].Country.value_counts().values.sum()/list_all[list_all.division_eu=='AC'].Country.value_counts().values.sum() * 100.
            len_eu14 = len(nam14)
            len_eu13 = len(nam13)
            len_ac = len(namac)
            plt.hlines(avg_eu14, xmin=0, xmax=len_eu14-1, color='tab:blue', ls='dashed', label="EU14 average")
            plt.hlines(avg_eu13, xmin=len_eu14, xmax=len_eu14+len_eu13-1, color='tab:orange', ls='dashed', label="EU13 average")
            plt.hlines(avg_ac, xmin=len_eu14+len_eu13, xmax=len_eu14+len_eu13+len_ac-1, color='tab:green', ls='dashed', label="AC average")
            handles, labels = ax1.get_legend_handles_labels()
            handles2, labels2 = ax2.get_legend_handles_labels()
            ax2.legend(handles + handles2, labels + labels2, loc=0)
            # plt.xticks(rotation=90)
            fig.tight_layout() 
            plt.title("Country success rate with number of proposals: " + topic_name + str(year_name) + " - per group")
            name_graph="country_success_rate_number_proposals_" + topic_name + str(year_name) + ".png"
            plt.savefig(name_graph, bbox_inches='tight', dpi=300)
            first_axis=score_df.Name[score_df.Division=='EU14'].to_string(index=False).split("\n")
            second_axis=score_df.Name[score_df.Division=='EU13'].to_string(index=False).split("\n")
            third_axis=score_df.Name[score_df.Division=='AC'].to_string(index=False).split("\n")
            name_axes=sorted(set(first_axis + second_axis + third_axis))
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

    elif group_type == "groups_with_avg_number_proposals_EU14":
        if topic_name=="ALL":
            # queries for participants and coordinators for ALL calls and years
            sql_main = """ SELECT * FROM Annex7T7_new WHERE Status="Main list" """
            list_main = pd.read_sql(sql_main,conn)
            # when looking for the total number of participation for some contry, we just dont take ineligible calls, everything else goes to sum.
            sql_all = """ SELECT * FROM Annex7T7_new WHERE Status!="Ineligible" """
            list_all = pd.read_sql(sql_all,conn)
            # we create 3 lists, 2 are empty for now
            country_name  = list_main.Country.value_counts().index.values.tolist()
            country_score = []
            country_on_main = []
            country_on_all = []
            division = []
            for x in country_name:
                ## to calculate sr (success rate) we need number of participation on main divided by all participation for each country.
                c_main = list_main.Country.value_counts()[list_main.Country.value_counts().index==x].values
                c_all = list_all.Country.value_counts()[list_all.Country.value_counts().index==x].values
                ## success rate is:
                sr = (c_main / c_all * 100.0)[0] ## sr is list so we need just first element that is why we use [0]
                country_score.append(sr)
                country_on_main.append(c_main[0])
                country_on_all.append(c_all[0])
                ## now with the list of country scores we need another list same length, with exactly which division that country is assigned.
                division.append(list_main[list_main.Country.values == x].division_eu.values[0])
            ## finaly we create a data frame score_df with 3 values in order to sort that and then plot.
            score_df = pd.DataFrame({"Name" : country_name, "Score" : country_score, "Division" : division,
                                      "Funded" : country_on_main, "Proposed" : country_on_all})
            score_df = score_df.sort_values(by=['Score'],ascending=False)

            fig = plt.figure(figsize=(14,6))
            #we plot bars with values from score_df Name and Score, acording to the group.
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.bar(score_df.Name[score_df.Division=='EU14'], score_df.Funded[score_df.Division=='EU14'], color='tab:blue',label='Funded',align='edge',width=-0.4) 
            ax1.bar(score_df.Name[score_df.Division=='EU14'], score_df.Proposed[score_df.Division=='EU14'], color='tab:cyan',label='Proposed',align='edge',width=0.4)
            ax2.scatter(score_df.Name[score_df.Division=='EU14'], score_df.Score[score_df.Division=='EU14'], c='tab:brown', label='Country success rate')
            nam = score_df.Name[score_df.Division=='EU14'].values.tolist()
            sco = score_df.Score[score_df.Division=='EU14'].values.tolist()
            for i, txt in enumerate(sco):
                ax2.annotate(np.round(sco[i],decimals=1), (nam[i],sco[i]+2), ha="center")
            # Now we calculate averages to add them to graph, and we also use nam14, nam13, namac
            avg_eu27 = list_main[list_main.division_eu27=='EU27'].Country.value_counts().values.sum()/list_all[list_all.division_eu27=='EU27'].Country.value_counts().values.sum() * 100.
            avg_eu14 = list_main[list_main.division_eu=='EU14'].Country.value_counts().values.sum()/list_all[list_all.division_eu=='EU14'].Country.value_counts().values.sum() * 100.
            len_eu14 = len(nam)
            plt.hlines(avg_eu27, xmin=0, xmax=len_eu14-1, color='tab:pink', ls='dashed', label="EU27 average")
            plt.hlines(avg_eu14, xmin=0, xmax=len_eu14-1, color='tab:purple', ls='dotted', label="EU14 average")
            handles, labels = ax1.get_legend_handles_labels()
            handles2, labels2 = ax2.get_legend_handles_labels()
            ax2.legend(handles + handles2, labels + labels2, loc=0)
            ax2.set_ylim(top=max(sco)+4)
            fig.tight_layout() 
            plt.title("Country success rate with number of proposals for EU14: all calls")
            name_graph="country_success_rate_EU14_all_calls.png"
            plt.savefig(name_graph, bbox_inches='tight', dpi=300)
            name_axes=score_df.Name[score_df.Division=='EU14'].to_string(index=False).split("\n")
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

        else:
            sql_main = """ SELECT * FROM Annex7T7_new WHERE Status="Main list" AND Topic LIKE """+ '"'+ topic_name + str(year_name) + """-SPACE%" """
            list_main = pd.read_sql(sql_main,conn)
            sql_all = """ SELECT * FROM Annex7T7_new WHERE Status!="Ineligible" AND Topic LIKE """+ '"'+ topic_name + str(year_name) + """-SPACE%" """
            list_all = pd.read_sql(sql_all,conn)
            # we create 3 lists, 2 are empty for now
            country_name  = list_main.Country.value_counts().index.values.tolist()
            country_score = []
            country_on_main = []
            country_on_all = []
            division = []
            for x in country_name:
                ## to calculate sr (success rate) we need number of participation on main divided by all participation for each country.
                c_main = list_main.Country.value_counts()[list_main.Country.value_counts().index==x].values
                c_all = list_all.Country.value_counts()[list_all.Country.value_counts().index==x].values
                ## success rate is:
                sr = (c_main / c_all * 100.0)[0] ## sr is list so we need just first element that is why we use [0]
                country_score.append(sr)
                country_on_main.append(c_main[0])
                country_on_all.append(c_all[0])
                ## now with the list of country scores we need another list same length, with exactly which division that country is assigned.
                division.append(list_main[list_main.Country.values == x].division_eu.values[0])
            ## finaly we create a data frame score_df with 3 values in order to sort that and then plot.
            score_df = pd.DataFrame({"Name" : country_name, "Score" : country_score, "Division" : division,
                                      "Funded" : country_on_main, "Proposed" : country_on_all})
            score_df = score_df.sort_values(by=['Score'],ascending=False)

            fig = plt.figure(figsize=(14,6))
            #we plot bars with values from score_df Name and Score, acording to the group.
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.bar(score_df.Name[score_df.Division=='EU14'], score_df.Funded[score_df.Division=='EU14'], color='tab:blue',label='Funded',align='edge',width=-0.4) 
            ax1.bar(score_df.Name[score_df.Division=='EU14'], score_df.Proposed[score_df.Division=='EU14'], color='tab:cyan',label='Proposed',align='edge',width=0.4)
            ax2.scatter(score_df.Name[score_df.Division=='EU14'], score_df.Score[score_df.Division=='EU14'], c='tab:brown', label='Country success rate')
            nam = score_df.Name[score_df.Division=='EU14'].values.tolist()
            sco = score_df.Score[score_df.Division=='EU14'].values.tolist()
            for i, txt in enumerate(sco):
                ax2.annotate(np.round(sco[i],decimals=1), (nam[i],sco[i]+2), ha="center")
            # Now we calculate averages to add them to graph, and we also use nam14, nam13, namac
            avg_eu27 = list_main[list_main.division_eu27=='EU27'].Country.value_counts().values.sum()/list_all[list_all.division_eu27=='EU27'].Country.value_counts().values.sum() * 100.
            avg_eu14 = list_main[list_main.division_eu=='EU14'].Country.value_counts().values.sum()/list_all[list_all.division_eu=='EU14'].Country.value_counts().values.sum() * 100.
            len_eu14 = len(nam)
            plt.hlines(avg_eu27, xmin=0, xmax=len_eu14-1, color='tab:pink', ls='dashed', label="EU27 average")
            plt.hlines(avg_eu14, xmin=0, xmax=len_eu14-1, color='tab:purple', ls='dotted', label="EU14 average")
            handles, labels = ax1.get_legend_handles_labels()
            handles2, labels2 = ax2.get_legend_handles_labels()
            ax2.legend(handles + handles2, labels + labels2, loc=0)
            ax2.set_ylim(top=max(sco)+4)
            fig.tight_layout() 
            plt.title("Country success rate with number of proposals for EU14: " + topic_name + str(year_name))
            name_graph="country_success_rate_EU14_" + topic_name + str(year_name) + ".png"
            plt.savefig(name_graph, bbox_inches='tight', dpi=300)
            name_axes=score_df.Name[score_df.Division=='EU14'].to_string(index=False).split("\n")
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

    elif group_type == "groups_with_avg_number_proposals_EU13":
        if topic_name=="ALL":
            # queries for participants and coordinators for ALL calls and years
            sql_main = """ SELECT * FROM Annex7T7_new WHERE Status="Main list" """
            list_main = pd.read_sql(sql_main,conn)
            # when looking for the total number of participation for some contry, we just dont take ineligible calls, everything else goes to sum.
            sql_all = """ SELECT * FROM Annex7T7_new WHERE Status!="Ineligible" """
            list_all = pd.read_sql(sql_all,conn)
            # we create 3 lists, 2 are empty for now
            country_name  = list_main.Country.value_counts().index.values.tolist()
            country_score = []
            country_on_main = []
            country_on_all = []
            division = []
            for x in country_name:
                ## to calculate sr (success rate) we need number of participation on main divided by all participation for each country.
                c_main = list_main.Country.value_counts()[list_main.Country.value_counts().index==x].values
                c_all = list_all.Country.value_counts()[list_all.Country.value_counts().index==x].values
                ## success rate is:
                sr = (c_main / c_all * 100.0)[0] ## sr is list so we need just first element that is why we use [0]
                country_score.append(sr)
                country_on_main.append(c_main[0])
                country_on_all.append(c_all[0])
                ## now with the list of country scores we need another list same length, with exactly which division that country is assigned.
                division.append(list_main[list_main.Country.values == x].division_eu.values[0])
            ## finaly we create a data frame score_df with 3 values in order to sort that and then plot.
            score_df = pd.DataFrame({"Name" : country_name, "Score" : country_score, "Division" : division,
                                      "Funded" : country_on_main, "Proposed" : country_on_all})
            score_df = score_df.sort_values(by=['Score'],ascending=False)

            fig = plt.figure(figsize=(14,6))
            #we plot bars with values from score_df Name and Score, acording to the group.
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.bar(score_df.Name[score_df.Division=='EU13'], score_df.Funded[score_df.Division=='EU13'], color='tab:blue',label='Funded',align='edge',width=-0.4) 
            ax1.bar(score_df.Name[score_df.Division=='EU13'], score_df.Proposed[score_df.Division=='EU13'], color='tab:cyan',label='Proposed',align='edge',width=0.4)
            ax2.scatter(score_df.Name[score_df.Division=='EU13'], score_df.Score[score_df.Division=='EU13'], c='tab:brown', label='Country success rate')
            nam = score_df.Name[score_df.Division=='EU13'].values.tolist()
            sco = score_df.Score[score_df.Division=='EU13'].values.tolist()
            for i, txt in enumerate(sco):
                ax2.annotate(np.round(sco[i],decimals=1), (nam[i],sco[i]+2), ha="center")
            # Now we calculate averages to add them to graph, and we also use nam14, nam13, namac
            avg_eu27 = list_main[list_main.division_eu27=='EU27'].Country.value_counts().values.sum()/list_all[list_all.division_eu27=='EU27'].Country.value_counts().values.sum() * 100.
            avg_eu13 = list_main[list_main.division_eu=='EU13'].Country.value_counts().values.sum()/list_all[list_all.division_eu=='EU13'].Country.value_counts().values.sum() * 100.
            len_eu13 = len(nam)
            plt.hlines(avg_eu27, xmin=0, xmax=len_eu13-1, color='tab:pink', ls='dashed', label="EU27 average")
            plt.hlines(avg_eu13, xmin=0, xmax=len_eu13-1, color='tab:purple', ls='dotted', label="EU13 average")
            handles, labels = ax1.get_legend_handles_labels()
            handles2, labels2 = ax2.get_legend_handles_labels()
            ax2.legend(handles + handles2, labels + labels2, loc=0)
            ax2.set_ylim(top=max(sco)+4)
            fig.tight_layout() 
            plt.title("Country success rate with number of proposals for EU13: all calls")
            name_graph="country_success_rate_EU13_all_calls.png"
            plt.savefig(name_graph, bbox_inches='tight', dpi=300)
            name_axes=score_df.Name[score_df.Division=='EU13'].to_string(index=False).split("\n")
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

        else:
            sql_main = """ SELECT * FROM Annex7T7_new WHERE Status="Main list" AND Topic LIKE """+ '"'+ topic_name + str(year_name) + """-SPACE%" """
            list_main = pd.read_sql(sql_main,conn)
            sql_all = """ SELECT * FROM Annex7T7_new WHERE Status!="Ineligible" AND Topic LIKE """+ '"'+ topic_name + str(year_name) + """-SPACE%" """
            list_all = pd.read_sql(sql_all,conn)
            # we create 3 lists, 2 are empty for now
            country_name  = list_main.Country.value_counts().index.values.tolist()
            country_score = []
            country_on_main = []
            country_on_all = []
            division = []
            for x in country_name:
                ## to calculate sr (success rate) we need number of participation on main divided by all participation for each country.
                c_main = list_main.Country.value_counts()[list_main.Country.value_counts().index==x].values
                c_all = list_all.Country.value_counts()[list_all.Country.value_counts().index==x].values
                ## success rate is:
                sr = (c_main / c_all * 100.0)[0] ## sr is list so we need just first element that is why we use [0]
                country_score.append(sr)
                country_on_main.append(c_main[0])
                country_on_all.append(c_all[0])
                ## now with the list of country scores we need another list same length, with exactly which division that country is assigned.
                division.append(list_main[list_main.Country.values == x].division_eu.values[0])
            ## finaly we create a data frame score_df with 3 values in order to sort that and then plot.
            score_df = pd.DataFrame({"Name" : country_name, "Score" : country_score, "Division" : division,
                                      "Funded" : country_on_main, "Proposed" : country_on_all})
            score_df = score_df.sort_values(by=['Score'],ascending=False)

            fig = plt.figure(figsize=(14,6))
            #we plot bars with values from score_df Name and Score, acording to the group.
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.bar(score_df.Name[score_df.Division=='EU13'], score_df.Funded[score_df.Division=='EU13'], color='tab:blue',label='Funded',align='edge',width=-0.4) 
            ax1.bar(score_df.Name[score_df.Division=='EU13'], score_df.Proposed[score_df.Division=='EU13'], color='tab:cyan',label='Proposed',align='edge',width=0.4)
            ax2.scatter(score_df.Name[score_df.Division=='EU13'], score_df.Score[score_df.Division=='EU13'], c='tab:brown', label='Country success rate')
            nam = score_df.Name[score_df.Division=='EU13'].values.tolist()
            sco = score_df.Score[score_df.Division=='EU13'].values.tolist()
            for i, txt in enumerate(sco):
                ax2.annotate(np.round(sco[i],decimals=1), (nam[i],sco[i]+2), ha="center")
            # Now we calculate averages to add them to graph, and we also use nam14, nam13, namac
            avg_eu27 = list_main[list_main.division_eu27=='EU27'].Country.value_counts().values.sum()/list_all[list_all.division_eu27=='EU27'].Country.value_counts().values.sum() * 100.
            avg_eu13 = list_main[list_main.division_eu=='EU13'].Country.value_counts().values.sum()/list_all[list_all.division_eu=='EU13'].Country.value_counts().values.sum() * 100.
            len_eu13 = len(nam)
            plt.hlines(avg_eu27, xmin=0, xmax=len_eu13-1, color='tab:pink', ls='dashed', label="EU27 average")
            plt.hlines(avg_eu13, xmin=0, xmax=len_eu13-1, color='tab:purple', ls='dotted', label="EU13 average")
            handles, labels = ax1.get_legend_handles_labels()
            handles2, labels2 = ax2.get_legend_handles_labels()
            ax2.legend(handles + handles2, labels + labels2, loc=0)
            ax2.set_ylim(top=max(sco)+4)
            fig.tight_layout() 
            plt.title("Country success rate with number of proposals for EU13: " + topic_name + str(year_name))
            name_graph="country_success_rate_EU13_" + topic_name + str(year_name) + ".png"
            plt.savefig(name_graph, bbox_inches='tight', dpi=300)
            name_axes=score_df.Name[score_df.Division=='EU13'].to_string(index=False).split("\n")
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()
            
    elif group_type == "groups_with_avg_number_proposals_AC":
        if topic_name=="ALL":
            # queries for participants and coordinators for ALL calls and years
            sql_main = """ SELECT * FROM Annex7T7_new WHERE Status="Main list" """
            list_main = pd.read_sql(sql_main,conn)
            # when looking for the total number of participation for some contry, we just dont take ineligible calls, everything else goes to sum.
            sql_all = """ SELECT * FROM Annex7T7_new WHERE Status!="Ineligible" """
            list_all = pd.read_sql(sql_all,conn)
            # we create 3 lists, 2 are empty for now
            country_name  = list_main.Country.value_counts().index.values.tolist()
            country_score = []
            country_on_main = []
            country_on_all = []
            division = []
            for x in country_name:
                ## to calculate sr (success rate) we need number of participation on main divided by all participation for each country.
                c_main = list_main.Country.value_counts()[list_main.Country.value_counts().index==x].values
                c_all = list_all.Country.value_counts()[list_all.Country.value_counts().index==x].values
                ## success rate is:
                sr = (c_main / c_all * 100.0)[0] ## sr is list so we need just first element that is why we use [0]
                country_score.append(sr)
                country_on_main.append(c_main[0])
                country_on_all.append(c_all[0])
                ## now with the list of country scores we need another list same length, with exactly which division that country is assigned.
                division.append(list_main[list_main.Country.values == x].division_eu.values[0])
            ## finaly we create a data frame score_df with 3 values in order to sort that and then plot.
            score_df = pd.DataFrame({"Name" : country_name, "Score" : country_score, "Division" : division,
                                      "Funded" : country_on_main, "Proposed" : country_on_all})
            score_df = score_df.sort_values(by=['Score'],ascending=False)

            fig = plt.figure(figsize=(14,6))
            #we plot bars with values from score_df Name and Score, acording to the group.
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.bar(score_df.Name[score_df.Division=='AC'], score_df.Funded[score_df.Division=='AC'], color='tab:blue',label='Funded',align='edge',width=-0.4) 
            ax1.bar(score_df.Name[score_df.Division=='AC'], score_df.Proposed[score_df.Division=='AC'], color='tab:cyan',label='Proposed',align='edge',width=0.4)
            ax2.scatter(score_df.Name[score_df.Division=='AC'], score_df.Score[score_df.Division=='AC'], c='tab:brown', label='Country success rate')
            nam = score_df.Name[score_df.Division=='AC'].values.tolist()
            sco = score_df.Score[score_df.Division=='AC'].values.tolist()
            for i, txt in enumerate(sco):
                ax2.annotate(np.round(sco[i],decimals=1), (nam[i],sco[i]+2), ha="center")
            # Now we calculate averages to add them to graph, and we also use nam14, nam13, namac
            avg_eu27 = list_main[list_main.division_eu27=='EU27'].Country.value_counts().values.sum()/list_all[list_all.division_eu27=='EU27'].Country.value_counts().values.sum() * 100.
            avg_ac = list_main[list_main.division_eu=='AC'].Country.value_counts().values.sum()/list_all[list_all.division_eu=='AC'].Country.value_counts().values.sum() * 100.
            len_ac = len(nam)
            plt.hlines(avg_eu27, xmin=0, xmax=len_ac-1, color='tab:pink', ls='dashed', label="EU27 average")
            plt.hlines(avg_ac, xmin=0, xmax=len_ac-1, color='tab:purple', ls='dotted', label="AC average")
            handles, labels = ax1.get_legend_handles_labels()
            handles2, labels2 = ax2.get_legend_handles_labels()
            ax2.legend(handles + handles2, labels + labels2, loc=0)
            ax2.set_ylim(top=max(sco)+4)
            fig.tight_layout() 
            plt.title("Country success rate with number of proposals for AC: all calls")
            name_graph="country_success_rate_AC_all_calls.png"
            plt.savefig(name_graph, bbox_inches='tight', dpi=300)
            name_axes=score_df.Name[score_df.Division=='AC'].to_string(index=False).split("\n")
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

        else:
            sql_main = """ SELECT * FROM Annex7T7_new WHERE Status="Main list" AND Topic LIKE """+ '"'+ topic_name + str(year_name) + """-SPACE%" """
            list_main = pd.read_sql(sql_main,conn)
            sql_all = """ SELECT * FROM Annex7T7_new WHERE Status!="Ineligible" AND Topic LIKE """+ '"'+ topic_name + str(year_name) + """-SPACE%" """
            list_all = pd.read_sql(sql_all,conn)
            # we create 3 lists, 2 are empty for now
            country_name  = list_main.Country.value_counts().index.values.tolist()
            country_score = []
            country_on_main = []
            country_on_all = []
            division = []
            for x in country_name:
                ## to calculate sr (success rate) we need number of participation on main divided by all participation for each country.
                c_main = list_main.Country.value_counts()[list_main.Country.value_counts().index==x].values
                c_all = list_all.Country.value_counts()[list_all.Country.value_counts().index==x].values
                ## success rate is:
                sr = (c_main / c_all * 100.0)[0] ## sr is list so we need just first element that is why we use [0]
                country_score.append(sr)
                country_on_main.append(c_main[0])
                country_on_all.append(c_all[0])
                ## now with the list of country scores we need another list same length, with exactly which division that country is assigned.
                division.append(list_main[list_main.Country.values == x].division_eu.values[0])
            ## finaly we create a data frame score_df with 3 values in order to sort that and then plot.
            score_df = pd.DataFrame({"Name" : country_name, "Score" : country_score, "Division" : division,
                                      "Funded" : country_on_main, "Proposed" : country_on_all})
            score_df = score_df.sort_values(by=['Score'],ascending=False)

            fig = plt.figure(figsize=(14,6))
            #we plot bars with values from score_df Name and Score, acording to the group.
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.bar(score_df.Name[score_df.Division=='AC'], score_df.Funded[score_df.Division=='AC'], color='tab:blue',label='Funded',align='edge',width=-0.4) 
            ax1.bar(score_df.Name[score_df.Division=='AC'], score_df.Proposed[score_df.Division=='AC'], color='tab:cyan',label='Proposed',align='edge',width=0.4)
            ax2.scatter(score_df.Name[score_df.Division=='AC'], score_df.Score[score_df.Division=='AC'], c='tab:brown', label='Country success rate')
            nam13 = score_df.Name[score_df.Division=='AC'].values.tolist()
            nam = nam13
            sco = score_df.Score[score_df.Division=='AC'].values.tolist()
            for i, txt in enumerate(sco):
                ax2.annotate(np.round(sco[i],decimals=1), (nam[i],sco[i]+2), ha="center")
            # Now we calculate averages to add them to graph, and we also use nam14, nam13, namac
            avg_eu27 = list_main[list_main.division_eu27=='EU27'].Country.value_counts().values.sum()/list_all[list_all.division_eu27=='EU27'].Country.value_counts().values.sum() * 100.
            avg_AC = list_main[list_main.division_eu=='AC'].Country.value_counts().values.sum()/list_all[list_all.division_eu=='AC'].Country.value_counts().values.sum() * 100.
            len_AC = len(nam13)
            plt.hlines(avg_eu27, xmin=0, xmax=len_AC-1, color='tab:pink', ls='dashed', label="EU27 average")
            plt.hlines(avg_AC, xmin=0, xmax=len_AC-1, color='tab:purple', ls='dotted', label="AC average")
            handles, labels = ax1.get_legend_handles_labels()
            handles2, labels2 = ax2.get_legend_handles_labels()
            ax2.legend(handles + handles2, labels + labels2, loc=0)
            ax2.set_ylim(top=max(sco)+4)
            fig.tight_layout() 
            plt.title("Country success rate with number of proposals for AC: " + topic_name + str(year_name))
            name_graph="country_success_rate_AC_" + topic_name + str(year_name) + ".png"
            plt.savefig(name_graph, bbox_inches='tight', dpi=300)
            name_axes=score_df.Name[score_df.Division=='AC'].to_string(index=False).split("\n")
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

    elif group_type == "groups_with_avg_number_proposals_WD":
        if topic_name=="ALL":
            sql_main = """ SELECT * FROM Annex7T7_new WHERE Status="Main list" """
            list_main = pd.read_sql(sql_main,conn)
            sql_all = """ SELECT * FROM Annex7T7_new WHERE Status!="Ineligible" """
            list_all = pd.read_sql(sql_all,conn)
            country_name  = list_main.Country.value_counts().index.values.tolist()
            country_score = []
            country_on_main = []
            country_on_all = []
            division = []
            for x in country_name:
                c_main = list_main.Country.value_counts()[list_main.Country.value_counts().index==x].values
                c_all = list_all.Country.value_counts()[list_all.Country.value_counts().index==x].values
                sr = (c_main / c_all * 100.0)[0] ## sr is list so we need just first element that is why we use [0]
                country_score.append(sr)
                country_on_main.append(c_main[0])
                country_on_all.append(c_all[0])
                division.append(list_main[list_main.Country.values == x].division_wd.values[0])
            score_df = pd.DataFrame({"Name" : country_name, "Score" : country_score, "Division" : division,
                                      "Funded" : country_on_main, "Proposed" : country_on_all})
            score_df = score_df.sort_values(by=['Score'],ascending=False)
            
            fig = plt.figure(figsize=(14,6))
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.bar(score_df.Name[score_df.Division=='WD'], score_df.Funded[score_df.Division=='WD'], color='tab:blue',label='Funded',align='edge',width=-0.4) 
            ax1.bar(score_df.Name[score_df.Division=='WD'], score_df.Proposed[score_df.Division=='WD'], color='tab:cyan',label='Proposed',align='edge',width=0.4)
            ax2.scatter(score_df.Name[score_df.Division=='WD'], score_df.Score[score_df.Division=='WD'], c='tab:brown')
            nam = score_df.Name[score_df.Division=='WD'].values.tolist()
            sco = score_df.Score[score_df.Division=='WD'].values.tolist()
            for i, txt in enumerate(sco):
                ax2.annotate(np.round(sco[i],decimals=1), (nam[i],sco[i]+2), ha="center")
            avg_eu27 = list_main[list_main.division_eu27=='EU27'].Country.value_counts().values.sum()/list_all[list_all.division_eu27=='EU27'].Country.value_counts().values.sum() * 100.
            avg_wd = list_main[list_main.division_wd=='WD'].Country.value_counts().values.sum()/list_all[list_all.division_wd=='WD'].Country.value_counts().values.sum() * 100.
            len_wd = len(nam)
            plt.hlines(avg_eu27, xmin=0, xmax=len_wd-1, color='tab:pink', ls='dashed', label="EU27 average")
            plt.hlines(avg_wd, xmin=0, xmax=len_wd-1, color='tab:purple', ls='dotted', label="WD average")
            handles, labels = ax1.get_legend_handles_labels()
            handles2, labels2 = ax2.get_legend_handles_labels()
            ax2.legend(handles + handles2, labels + labels2, loc=0)
            ax2.set_ylim(top=max(sco)+5)
            # plt.xticks(rotation=90)
            fig.tight_layout() 
            plt.title("Country success rate with number of proposals for WD: all calls")
            name_graph="country_success_rate_WD_all_calls.png"
            plt.savefig(name_graph, bbox_inches='tight', dpi=300)
            name_axes=score_df.Name[score_df.Division=='WD'].to_string(index=False).split("\n")
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

        else:
            sql_main = """ SELECT * FROM Annex7T7_new WHERE Status="Main list" AND Topic LIKE """+ '"'+ topic_name + str(year_name) + """-SPACE%" """
            list_main = pd.read_sql(sql_main,conn)
            sql_all = """ SELECT * FROM Annex7T7_new WHERE Status!="Ineligible" AND Topic LIKE """+ '"'+ topic_name + str(year_name) + """-SPACE%" """
            list_all = pd.read_sql(sql_all,conn)
            country_name  = list_main.Country.value_counts().index.values.tolist()
            country_score = []
            country_on_main = []
            country_on_all = []
            division = []
            for x in country_name:
                c_main = list_main.Country.value_counts()[list_main.Country.value_counts().index==x].values
                c_all = list_all.Country.value_counts()[list_all.Country.value_counts().index==x].values
                sr = (c_main / c_all * 100.0)[0] ## sr is list so we need just first element that is why we use [0]
                country_score.append(sr)
                country_on_main.append(c_main[0])
                country_on_all.append(c_all[0])
                division.append(list_main[list_main.Country.values == x].division_wd.values[0])
            score_df = pd.DataFrame({"Name" : country_name, "Score" : country_score, "Division" : division,
                                      "Funded" : country_on_main, "Proposed" : country_on_all})
            score_df = score_df.sort_values(by=['Score'],ascending=False)
            
            fig = plt.figure(figsize=(14,6))
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.bar(score_df.Name[score_df.Division=='WD'], score_df.Funded[score_df.Division=='WD'], color='tab:blue',label='Funded',align='edge',width=-0.4) 
            ax1.bar(score_df.Name[score_df.Division=='WD'], score_df.Proposed[score_df.Division=='WD'], color='tab:cyan',label='Proposed',align='edge',width=0.4)
            ax2.scatter(score_df.Name[score_df.Division=='WD'], score_df.Score[score_df.Division=='WD'], c='tab:brown')
            nam = score_df.Name[score_df.Division=='WD'].values.tolist()
            sco = score_df.Score[score_df.Division=='WD'].values.tolist()
            for i, txt in enumerate(sco):
                ax2.annotate(np.round(sco[i],decimals=1), (nam[i],sco[i]+2), ha="center")
            avg_eu27 = list_main[list_main.division_eu27=='EU27'].Country.value_counts().values.sum()/list_all[list_all.division_eu27=='EU27'].Country.value_counts().values.sum() * 100.
            avg_wd = list_main[list_main.division_wd=='WD'].Country.value_counts().values.sum()/list_all[list_all.division_wd=='WD'].Country.value_counts().values.sum() * 100.
            len_wd = len(nam)
            plt.hlines(avg_eu27, xmin=0, xmax=len_wd-1, color='tab:pink', ls='dashed', label="EU27 average")
            plt.hlines(avg_wd, xmin=0, xmax=len_wd-1, color='tab:purple', ls='dotted', label="WD average")
            handles, labels = ax1.get_legend_handles_labels()
            handles2, labels2 = ax2.get_legend_handles_labels()
            ax2.legend(handles + handles2, labels + labels2, loc=0)
            ax2.set_ylim(top=max(sco)+5)
            # plt.xticks(rotation=90)
            fig.tight_layout() 
            plt.title("Country success rate with number of proposals for WD: " + topic_name + str(year_name))
            name_graph="country_success_rate_WD_" + topic_name + str(year_name) + ".png"
            plt.savefig(name_graph, bbox_inches='tight', dpi=300)
            name_axes=score_df.Name[score_df.Division=='WD'].to_string(index=False).split("\n")
            print(name_graph,' '.join(name_axes), file=x_axis_file)
            plt.close()

    else:
        # finally if none of the options is matched then error statement is printed.
        print("ERROR - you have selected group_type that is not supported by this function.")
    x_axis_file.close()

### ------------ END OF FUNCTION SUCCESS RATE ----------------------------------





# =============================================================================
# ------------------- MAIN PROGRAM --------------------------------------------
# =============================================================================
import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.table as mtable

# =============================================================================
# declare and read database
# =============================================================================
db_name = "HorizonSpaceDB_new"
conn = sqlite3.connect(db_name + '.sqlite')
# path name should be changed at the begining and then used for all functions
# path_name_milan = "E:\\Dropbox\\Cosmos4HE\\milan\\02_plots\\"
path_name_milan = "C:\\Users\\milan\\Dropbox\\Cosmos4HE\\milan\\02_plots\\"
# path_name_ana = "/Users/anavudragovic/Dropbox/Cosmos4HE/milan/01_programs/"
# path_name_milena = " ... "


# =============================================================================
# --------------------------- Total Costs -------------------------------------
# arguments in order:
# path_name must be changed at the begining  
# topic_name (ALL, HORIZON-CL4-, HORIZON-EUSPA-),
# year_name (ALL, 2021, 2022),
# group_type(coordination, division_eu, widening) unosi se kao treci argument ali je ubacen na pocetku da zameni sve pozive odjednom
# group_type coordination means separate graphs for coordinators and participants, while
# group_type division_eu means separate graphs for each of EU14, EU13, AC, OTH
# =============================================================================
# groups=["coordination", "division_eu", "widening"]
# for i in range(len(groups)):
#     total_costs(path_name_milan,"ALL","ALL",groups[i])
#     total_costs(path_name_milan,"HORIZON-CL4-","2021",groups[i])
#     total_costs(path_name_milan,"HORIZON-CL4-","2022",groups[i])
#     total_costs(path_name_milan,"HORIZON-CL4-","2023",groups[i])
#     total_costs(path_name_milan,"HORIZON-CL4-","2024",groups[i])  ### this will include partnership iba
#     total_costs(path_name_milan,"HORIZON-EUSPA-","2021",groups[i])
#     total_costs(path_name_milan,"HORIZON-EUSPA-","2022",groups[i])
#     total_costs(path_name_milan,"HORIZON-EUSPA-","2023",groups[i])


# =============================================================================
# --------------------------- Participation Count -----------------------------
# path_name must be changed at the begining 
### topic_name (ALL, HORIZON-CL4-, HORIZON-EUSPA-), year_name (ALL, 2021, 2022), group_type
### group_type(coordination,       # separate graphs for coordinators and participants
###             coordination_EU14, # -- || -- but only EU14 countries
###             coordination_EU13, # -- || --          EU13
###             coordination_AC,   # -- || --
###             coordination_WD,   # -- || --
###             division_eu,       # All goups EU14, EU13, AC, OTH on one graph without separation between Coo and Part
###             widening)          # Combined Coo and part
# # =============================================================================
# groups=["coordination", "coordination_EU14", "coordination_EU13", "coordination_AC", "coordination_WD", "division_eu", "widening"]
# for i in range(len(groups)):
#     participation_count(path_name_milan,"ALL","ALL",groups[i])
#     participation_count(path_name_milan,"HORIZON-CL4-","2021",groups[i])
#     participation_count(path_name_milan,"HORIZON-CL4-","2022",groups[i])
#     participation_count(path_name_milan,"HORIZON-CL4-","2023",groups[i])
#     participation_count(path_name_milan,"HORIZON-CL4-","2024",groups[i])
#     participation_count(path_name_milan,"HORIZON-EUSPA-","2021",groups[i])
#     participation_count(path_name_milan,"HORIZON-EUSPA-","2022",groups[i])
#     participation_count(path_name_milan,"HORIZON-EUSPA-","2023",groups[i])


# =============================================================================
# --------------------------- Legal Type -----------------------------
# topic_name (ALL, HORIZON-CL4-, HORIZON-EUSPA-), year_name (ALL, 2021, 2022), 
# group_type:
# coordination, division_eu, widening
# another group_type = "pie" for pie charts
# =============================================================================
# groups=["coordination","division_eu","widening","pie"]
# for i in range(len(groups)):
#     legal_type(path_name_milan,"ALL","ALL",groups[i])
#     legal_type(path_name_milan,"HORIZON-CL4-","2021",groups[i])
#     legal_type(path_name_milan,"HORIZON-CL4-","2022",groups[i])
#     legal_type(path_name_milan,"HORIZON-CL4-","2023",groups[i])
#     legal_type(path_name_milan,"HORIZON-CL4-","2024",groups[i])
#     legal_type(path_name_milan,"HORIZON-EUSPA-","2021",groups[i])
#     legal_type(path_name_milan,"HORIZON-EUSPA-","2022",groups[i])
#     legal_type(path_name_milan,"HORIZON-EUSPA-","2023",groups[i])


# =============================================================================
# --------------------------- Country Groups-----------------------------------
# topic_name (ALL, HORIZON-CL4-, HORIZON-EUSPA-), year_name (ALL, 2021, 2022), 
# group_type:
# coordination_table, type_of_action
# =============================================================================
# group=["coordination_table", "type_of_action"]
# for i in range(len(groups)):
#     country_groups(path_name_milan,"ALL","ALL",groups[i])
#     country_groups(path_name_milan,"HORIZON-CL4-","2021",groups[i])
#     country_groups(path_name_milan,"HORIZON-CL4-","2022",groups[i])
#     country_groups(path_name_milan,"HORIZON-CL4-","2023",groups[i])
#     country_groups(path_name_milan,"HORIZON-CL4-","2024",groups[i])
#     country_groups(path_name_milan,"HORIZON-EUSPA-","2021",groups[i])
#     country_groups(path_name_milan,"HORIZON-EUSPA-","2022",groups[i])
#     country_groups(path_name_milan,"HORIZON-EUSPA-","2023",groups[i])


# =============================================================================
# --------------------------- Success rate-----------------------------------
# topic_name (ALL, HORIZON-CL4-, HORIZON-EUSPA-), year_name (ALL, 2021, 2022), 
# group_type:
# groups_with_avg
# groups_with_avg_number_proposals
# groups_with_avg_number_proposals_EU14
# groups_with_avg_number_proposals_EU13
# groups_with_avg_number_proposals_AC
# groups_with_avg_number_proposals_WD
# =============================================================================
# groups=["groups_with_avg", "groups_with_avg_number_proposals", "groups_with_avg_number_proposals_EU14", "groups_with_avg_number_proposals_EU13", "groups_with_avg_number_proposals_AC", "groups_with_avg_number_proposals_WD"]
# for i in range(len(groups)):
#     success_rate(path_name_milan,"ALL","ALL",groups[i])
#     success_rate(path_name_milan,"HORIZON-CL4-","2021",groups[i])
#     success_rate(path_name_milan,"HORIZON-CL4-","2022",groups[i])
#     success_rate(path_name_milan,"HORIZON-CL4-","2023",groups[i])
#     success_rate(path_name_milan,"HORIZON-CL4-","2024",groups[i])
#     success_rate(path_name_milan,"HORIZON-EUSPA-","2021",groups[i])
#     success_rate(path_name_milan,"HORIZON-EUSPA-","2022",groups[i])
#     success_rate(path_name_milan,"HORIZON-EUSPA-","2023",groups[i])


# =============================================================================
# close database
# =============================================================================
print("----- Closing database -----")
conn.close()









### in case figure is cut in the title, add this to the savefig command:  bbox_inches='tight',

### ================ JUST FOR TESTING =========================================
# To test database without entering any of the functions use next: 
# dbname_test = "HorizonSpaceDB_new"
# conn_test = sqlite3.connect(dbname_test + '.sqlite')
### simple query that takes all data from Anex7T7, !!!! QUERY IS NOT CASE SENSITIVE, so "Type of Action" is same as "type of action"
# sql_test = """ SELECT * FROM Annex7T7_new """ # This query takes all Anex7T7 from the database, which means all calls on all lists.
### put everything from Query to pandas data frame
# data_test = pd.read_sql(sql_test, conn_test)
### print names of columns from data frame
# print(data_test.columns)     # to see the names of all columns in db use this line.
### Index(['index', 'Topic', 'Panel', 'Type of Action', 'Proposal number',
###         'Acronym', 'Title', 'Status', 'Participant role', 'Country',
###         'Business name', 'Legal name', 'Legal type', 'Is SME?', 'Total costs',
###         'Requested EU contribution', 'division_eu', 'division_wd',
###         'division_eu27'],
###        dtype='object')
# conn_test.close()
### to print all collumns names directly from DB use next 3 lines (this is procedure without putting the query first or creating pandas dataframe)
### pandas data frame name of columns IS CASE SENSITIVE
# cursor_test = conn_test.execute('select * from Annex7T7_new')
# names_test = list(map(lambda x: x[0], cursor_test.description))
# print(names_test)
### Additional lines for testing
# ---
# topic_name="HORIZON-CL4-"
# year_name="2022"
### ================ END TESTING ==============================================