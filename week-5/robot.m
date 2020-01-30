                %% START CODE BLOCK %%
                switch obj.current_state
                    case 3 % go to goal
                        % 'go_to_goal'
                        if obj.check_event('at_obstacle')
                            % witch to avoid obstacle
                            obj.switch_state('avoid_obstacles')
                        end
                        % this takes priority over 'at_obstacle'
                        if obj.check_event('at_goal')
                            obj.switch_to_state('stop')
                        end
                        % else continue
                    case 4
                        % 'avoid_obstacles'
                        if obj.check_event('obstacle_cleared')
                            obj.switch_state('go_to_goal')
                        end
                        if obj.check_event('at_goal')
                            obj.switch_to_state('stop')
                        end
                        % else continue avoiding obstacles
                    case 5
                        % 'ao_an_gtg'
                    otherwise % at 1 or 2, do hting
                        % 'stop' or 'go_to_angle'
                        obj.switch_to_state('stop');
                end

                %% END CODE BLOCK %%

                